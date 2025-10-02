from importlib import import_module, reload
from pathlib import Path


def test_block_style_globs_generate_agents(tmp_path, monkeypatch):
    module = import_module("scripts.sync_agents_rules")
    module = reload(module)

    repo_root = tmp_path
    rules_dir = repo_root / ".cursor" / "rules"
    rules_dir.mkdir(parents=True)

    (repo_root / "docs" / "foo").mkdir(parents=True)
    (repo_root / "linear" / "bar" / "baz").mkdir(parents=True)

    rule_file = rules_dir / "test-rule.mdc"
    rule_file.write_text(
        "---\n"
        "title: Test Rule\n"
        "globs:\n"
        "  - docs/foo\n"
        "  - linear/bar/**\n"
        "---\n",
        encoding="utf-8",
    )

    template = module.RuleTemplate(
        slug="test-rule",
        title="Example",
        body="Example body.",
    )

    monkeypatch.setattr(module, "REPO_ROOT", repo_root)
    monkeypatch.setattr(module, "RULES_DIR", rules_dir)
    monkeypatch.setattr(module, "TEMPLATES", {"test-rule": template})

    expected = module.build_expected_contents()
    module.write_files(expected)

    generated_paths = {path.relative_to(repo_root) for path in expected.keys()}
    assert Path("docs/foo/AGENTS.md") in generated_paths
    assert Path("linear/bar/AGENTS.md") in generated_paths
    assert Path("linear/bar/baz/AGENTS.md") in generated_paths

    for path in generated_paths:
        content = (repo_root / path).read_text(encoding="utf-8")
        assert module.GENERATOR_HEADER in content
        assert "Example body." in content
