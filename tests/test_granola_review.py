import pytest

from scripts.granola_review import (
    ensure_safe_output_path,
    generate_meeting_slug,
    normalize_date,
    normalize_priority,
    split_paste_blocks,
)


def test_split_paste_blocks_only_actions():
    text = """
    ## Action Items
    - **Refine playbook**
      - Owner: Alex
      - Due Date: 2025-10-02

    ## Decisions
    - **Adopt workflow**
    """
    actions, summary = split_paste_blocks(text)
    assert summary is None
    assert actions.startswith("## Action Items")
    assert "Adopt workflow" in actions


def test_split_paste_blocks_with_summary():
    text = """
    ## Action Items
    - **Refine playbook**
      - Owner: Alex

    ### Auto-generated Summary
    Overall outcome was positive.
    """
    actions, summary = split_paste_blocks(text)
    assert summary is not None
    assert "Refine playbook" in actions
    assert summary.lstrip().startswith("### Auto-generated Summary")


def test_normalize_date_common_formats():
    assert normalize_date("2025-10-02") == "2025-10-02"
    assert normalize_date("Oct 2, 2025") == "2025-10-02"
    assert normalize_date("2025-10-02T09:30:00Z") == "2025-10-02"


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("P0", "P0"),
        ("p1", "P1"),
        ("high", "P1"),
        ("Medium", "P2"),
        ("low", "P3"),
    ],
)
def test_normalize_priority_aliases(raw, expected):
    assert normalize_priority(raw) == expected


def test_normalize_priority_rejects_unknown():
    with pytest.raises(ValueError):
        normalize_priority("unknown")


def test_generate_meeting_slug_happy_path():
    slug = generate_meeting_slug("Weekly Ops Sync", "2025-10-02")
    assert slug == "2025-10-02-weekly-ops-sync"


def test_generate_meeting_slug_fallback_title():
    slug = generate_meeting_slug("!!!", "2025-10-02")
    assert slug == "2025-10-02-meeting"


@pytest.mark.parametrize(
    "path",
    [
        "docs/agents/session-notes/SN_20251002-weekly-ops-sync.md",
        "linear/tickets/drafts/20251002-weekly-ops-sync.md",
        "docs/global/Decision_Docket.md",
    ],
)
def test_ensure_safe_output_path_allows_expected_targets(path):
    assert str(ensure_safe_output_path(path)) == path


@pytest.mark.parametrize(
    "path",
    [
        "../../etc/passwd",
        "/tmp/output.md",
        "docs/global/Other.md",
        "docs/agents/../secrets.md",
    ],
)
def test_ensure_safe_output_path_rejects_invalid_targets(path):
    with pytest.raises(ValueError):
        ensure_safe_output_path(path)

