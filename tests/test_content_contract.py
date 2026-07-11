from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "lantern-life-manager"


class ContentContractTests(unittest.TestCase):
    def test_global_untrusted_content_rule_loads_before_routing(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8").casefold()
        core = text.split("## route the request", 1)[0]

        for required in (
            "external content",
            "untrusted data",
            "disclose private data",
            "bypass approval",
        ):
            self.assertIn(required, core)

    def test_skill_routes_every_core_workflow(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8").casefold()

        for required in (
            "guided onboarding",
            "domain snapshot",
            "work request",
            "recover",
            "capability",
            "model",
        ):
            self.assertIn(required, text)

    def test_skill_description_is_trigger_only(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn(
            "description: Use when someone wants ongoing help coordinating",
            text,
        )

    def test_domain_snapshot_is_versioned_and_freshness_aware(self):
        text = (
            SKILL / "assets" / "templates" / "domain-snapshot.md"
        ).read_text(encoding="utf-8")

        for required in (
            "lantern-domain/v1",
            "Last verified",
            "Review after",
            "Supersedes",
        ):
            self.assertIn(required, text)

    def test_domain_snapshot_matches_approved_compact_schema(self):
        text = (
            SKILL / "assets" / "templates" / "domain-snapshot.md"
        ).read_text(encoding="utf-8")
        fields = [
            line
            for line in text.splitlines()
            if line.startswith("- ")
        ]

        self.assertEqual(
            fields,
            [
                "- Schema: lantern-domain/v1",
                "- Domain ID:",
                "- Status: active | waiting | blocked | completed | archived",
                "- Outcome:",
                "- Current state:",
                "- Done since last snapshot:",
                "- Blockers or decisions needed:",
                "- Next action:",
                "- Important dates:",
                "- Pending requests:",
                "- Confidence: high | medium | low",
                "- Last verified:",
                "- Review after:",
                "- Supersedes:",
            ],
        )

    def test_dashboard_example_matches_header_width(self):
        lines = (
            SKILL / "assets" / "templates" / "dashboard.md"
        ).read_text(encoding="utf-8").splitlines()
        table = [line for line in lines if line.startswith("|")]

        self.assertGreaterEqual(len(table), 3)
        width = table[0].count("|")
        self.assertTrue(all(line.count("|") == width for line in table))

    def test_architecture_uses_separate_projects_and_library_snapshots(self):
        text = (SKILL / "references" / "architecture.md").read_text(
            encoding="utf-8"
        ).casefold()

        for required in (
            "separate project",
            "chatgpt library",
            "append-only",
            "cannot wake",
        ):
            self.assertIn(required, text)

    def test_safety_requires_exact_action_approval(self):
        text = (
            SKILL / "references" / "safety-and-permissions.md"
        ).read_text(encoding="utf-8").casefold()

        for required in (
            "exact target",
            "ask again",
            "untrusted content",
            "academic integrity",
            "fabricate",
        ):
            self.assertIn(required, text)

    def test_model_routing_is_cost_sensitive_without_overclaiming(self):
        routing = (SKILL / "references" / "model-routing.md").read_text(
            encoding="utf-8"
        ).casefold()

        for required in (
            "cost-sensitive personal-plan heuristic",
            "official default",
            "model and reasoning effort are separate",
            "normal ceiling",
            "parallel subagents",
            "not a smarter rung",
            "api cost charts",
            "plus allowance",
        ):
            self.assertIn(required, routing)

        for path in (
            ROOT / "project-kit" / "LIFE_MANAGER_INSTRUCTIONS.md",
            ROOT / "project-kit" / "DOMAIN_COORDINATOR_INSTRUCTIONS.md",
        ):
            text = path.read_text(encoding="utf-8").casefold()
            self.assertIn("sol medium", text)
            self.assertIn("normal ceiling", text)
            self.assertIn("ultra", text)
            self.assertIn("parallel", text)

    def test_onboarding_builds_the_framework_before_domain_drilldown(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (
            ROOT / "project-kit" / "LIFE_MANAGER_INSTRUCTIONS.md"
        ).read_text(encoding="utf-8").casefold()

        for text in (onboarding, manager):
            for required in (
                "framework-first",
                "minimum domain inventory",
                "framework-ready checklist",
                "do not wait for the user to say continue",
                "before domain drilldown",
            ):
                self.assertIn(required, text)

    def test_onboarding_prefers_parallel_framework_setup_with_safe_fallback(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (
            ROOT / "project-kit" / "LIFE_MANAGER_INSTRUCTIONS.md"
        ).read_text(encoding="utf-8").casefold()

        for text in (onboarding, manager):
            for required in (
                "background setup task",
                "guided interview",
                "sequential fallback",
                "default framework",
                "never claim",
                "verified",
                "consolidated",
                "do not create speculative",
            ):
                self.assertIn(required, text)

    def test_toolchain_guidance_separates_lantern_from_codex_prerequisites(self):
        capability = (SKILL / "references" / "capability-setup.md").read_text(
            encoding="utf-8"
        ).casefold()
        install = (ROOT / "docs" / "INSTALL.md").read_text(
            encoding="utf-8"
        ).casefold()

        for text in (capability, install):
            for required in (
                "lantern itself does not require git",
                "lantern itself does not require python",
                "codex-assisted setup may require",
                "apple developer tools",
                "xcode",
                "windows",
                "project kit",
            ):
                self.assertIn(required, text)
        self.assertIn("bundled git", capability)

    def test_browser_auth_guidance_is_surface_aware(self):
        capability = (SKILL / "references" / "capability-setup.md").read_text(
            encoding="utf-8"
        ).casefold()
        troubleshooting = (ROOT / "docs" / "TROUBLESHOOTING.md").read_text(
            encoding="utf-8"
        ).casefold()

        for text in (capability, troubleshooting):
            self.assertIn("work app", text)
            self.assertIn("browser session", text)
            self.assertIn("open the actual page", text)
            self.assertIn("verify", text)
        self.assertIn("do not claim a tab is open", capability)

    def test_runtime_archive_has_no_executable_files(self):
        forbidden = [
            path
            for path in SKILL.rglob("*")
            if path.is_file()
            and path.suffix.lower()
            not in {".md", ".yaml", ".yml", ".json", ".txt"}
        ]

        self.assertEqual(forbidden, [])

    def test_project_kit_templates_match_runtime_templates(self):
        for name in (
            "domain-snapshot.md",
            "work-request.md",
            "dashboard.md",
            "onboarding-checkpoint.md",
        ):
            runtime = (SKILL / "assets" / "templates" / name).read_bytes()
            project = (
                ROOT / "project-kit" / "templates" / name
            ).read_bytes()

            self.assertEqual(project, runtime)

    def test_onboarding_checkpoint_and_recovery_are_durable(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        ).casefold()
        architecture = (SKILL / "references" / "architecture.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (
            ROOT / "project-kit" / "LIFE_MANAGER_INSTRUCTIONS.md"
        ).read_text(encoding="utf-8").casefold()

        for text in (onboarding, architecture, manager):
            self.assertIn("onboarding checkpoint", text)
            self.assertIn("lantern-onboarding/v1", text)
        self.assertIn("newest valid onboarding checkpoint", architecture)

    def test_project_kit_gives_domain_projects_their_templates(self):
        start = (ROOT / "project-kit" / "START_HERE.md").read_text(
            encoding="utf-8"
        ).casefold()
        install = (ROOT / "docs" / "INSTALL.md").read_text(
            encoding="utf-8"
        ).casefold()

        for text in (start, install):
            self.assertIn("each domain project", text)
            self.assertIn("domain-snapshot.md", text)
            self.assertIn("work-request.md", text)
            self.assertIn("cannot see files uploaded", text)

    def test_portable_export_is_a_runtime_workflow(self):
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8").casefold()
        architecture = (SKILL / "references" / "architecture.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (
            ROOT / "project-kit" / "LIFE_MANAGER_INSTRUCTIONS.md"
        ).read_text(encoding="utf-8").casefold()

        self.assertIn("export", skill)
        self.assertIn("references/architecture.md", skill)
        for text in (architecture, manager):
            self.assertIn("portable export", text)
            self.assertIn("latest dashboard", text)
            self.assertIn("open work requests", text)

    def test_project_kit_preserves_manager_and_domain_boundaries(self):
        manager = (
            ROOT / "project-kit" / "LIFE_MANAGER_INSTRUCTIONS.md"
        ).read_text(encoding="utf-8").casefold()
        domain = (
            ROOT / "project-kit" / "DOMAIN_COORDINATOR_INSTRUCTIONS.md"
        ).read_text(encoding="utf-8").casefold()

        self.assertIn("life manager", manager)
        self.assertIn("separate project", manager)
        self.assertIn("domain coordinator", domain)
        self.assertIn("publish", domain)


if __name__ == "__main__":
    unittest.main()
