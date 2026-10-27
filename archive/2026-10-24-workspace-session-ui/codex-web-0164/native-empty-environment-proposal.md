# Empty-environment registration restoration proposal

Status: source-supported proposal only; no source patch, native build or probe.

Frozen source: Codex 0.164.0 `6aaac694803004a63c6f393d153c96d22521a6b9`; old source is the exact retained 0.163.0 tree.

## Exact old/new guard hunks

### core/src/tools/spec_plan.rs

```diff
--- 0.163.0/core/src/tools/spec_plan.rs
+++ 0.164.0/core/src/tools/spec_plan.rs
@@ -154,6 +154,7 @@
         apps_enabled,
         &mcp.config().mcp_server_catalog,
         model_info.supports_search_tool,
+        session.services.mcp_manager.shared_definitions(),
         &mut registry,
     );
     apply_mcp_tool_exposure_policy(
@@ -1206,20 +1207,9 @@
                 .enabled(Feature::StandaloneWebSearch))
 }
 
-fn tool_environment_mode(context: &CoreToolPlanContext<'_>) -> ToolEnvironmentMode {
-    let count = if context
-        .turn_context
-        .config
-        .features
-        .get()
-        .enabled(Feature::StableEnvironmentTools)
-    {
-        // Keep selectors stable as selected attachments change readiness.
-        context.environments.environments.len()
-    } else {
-        context.environments.turn_environments().count()
-    };
-    ToolEnvironmentMode::from_count(count)
+fn tool_environment_mode(environments: &TurnEnvironmentSnapshot) -> ToolEnvironmentMode {
+    // Keep environment selectors stable as selected attachments change readiness.
+    ToolEnvironmentMode::from_count(environments.environments.len())
 }
 
 fn should_include_windows_shell_guidance(environments: &TurnEnvironmentSnapshot) -> bool {
@@ -1245,12 +1235,8 @@
 fn add_shell_tools(context: &CoreToolPlanContext<'_>, registry: &mut ToolRegistry) {
     let turn_context = context.turn_context;
     let features = turn_context.config.features.get();
-    let environment_mode = tool_environment_mode(context);
-    let stable_environment_tools = features.enabled(Feature::StableEnvironmentTools);
-    let advertise_environment_tools =
-        stable_environment_tools || environment_mode.has_environment();
-    if !advertise_environment_tools
-        || !features.enabled(Feature::ShellTool)
+    let environment_mode = tool_environment_mode(context.environments);
+    if !features.enabled(Feature::ShellTool)
         || matches!(context.model_info.shell_type, ConfigShellToolType::Disabled)
     {
         return;
@@ -1263,12 +1249,6 @@
         && context.tool_policy.expose_additional_permissions;
     let include_environment_id = matches!(environment_mode, ToolEnvironmentMode::Multiple);
     let options = ExecCommandHandlerOptions {
-        include_login_parameter: stable_environment_tools
-            || context
-                .environments
-                .turn_environments()
-                .any(|environment| environment.config().allow_login_shell),
-        include_shell_parameter: true,
         allow_tty: features.enabled(Feature::UnifiedExecTty),
         exec_permission_approvals_enabled,
         include_environment_id,
@@ -1307,10 +1287,7 @@
 fn add_core_utility_tools(context: &CoreToolPlanContext<'_>, registry: &mut ToolRegistry) {
     let turn_context = context.turn_context;
     let features = turn_context.config.features.get();
-    let environment_mode = tool_environment_mode(context);
-    let stable_environment_tools = features.enabled(Feature::StableEnvironmentTools);
-    let advertise_environment_tools =
-        stable_environment_tools || environment_mode.has_environment();
+    let environment_mode = tool_environment_mode(context.environments);
 
     if turn_context.config.update_plan_enabled {
         registry.add(PlanHandler);
@@ -1376,7 +1353,7 @@
         registry.add_with_exposure(SendMessageToUserAsyncHandler, ToolExposure::DirectModelOnly);
     }
 
-    if advertise_environment_tools && features.enabled(Feature::RequestPermissionsTool) {
+    if features.enabled(Feature::RequestPermissionsTool) {
         registry.add(RequestPermissionsHandler);
     }
 
@@ -1429,7 +1406,7 @@
         ));
     }
 
-    if advertise_environment_tools && context.model_info.apply_patch_tool_type.is_some() {
+    if context.model_info.apply_patch_tool_type.is_some() {
         let include_environment_id = matches!(environment_mode, ToolEnvironmentMode::Multiple);
         registry.add(ApplyPatchHandler::new(include_environment_id));
     }
@@ -1443,7 +1420,7 @@
         registry.add(TestSyncHandler);
     }
 
-    if advertise_environment_tools && features.enabled(Feature::ViewImage) {
+    if features.enabled(Feature::ViewImage) {
         let include_environment_id = matches!(environment_mode, ToolEnvironmentMode::Multiple);
         registry.add(ViewImageHandler::new(ViewImageToolOptions {
             can_request_original_image_detail: can_request_original_image_detail(
```

### features/src/lib.rs

```diff
@@ -117,11 +120,15 @@
 
     /// Automatically start the shared local daemon for eligible interactive launches.
     DaemonAutoStart,
+    /// Enable negotiated zstd compression for app-server WebSocket and UDS connections.
+    AppServerWebSocketCompression,
 
     // Experimental
     /// Advertise enabled environment-backed tools and their shell parameters before the
     /// executor is ready. Actual execution still requires a usable environment and its policy.
     StableEnvironmentTools,
+    /// Copy files between explicitly selected execution environments.
+    MultiEnvCopyFile,
     /// Send per-content-entry classifications in internal Responses metadata.
     ContentItemKinds,
     /// Record model-attempted tool calls in internal Responses metadata.
@@ -1153,7 +1191,7 @@
     FeatureSpec {
         id: Feature::StableEnvironmentTools,
         key: "stable_environment_tools",
-        stage: Stage::UnderDevelopment,
+        stage: Stage::Removed,
         default_enabled: false,
     },
     FeatureSpec {
```

### tools/src/tool_config.rs

```diff
(unchanged)
```

Unchanged exact mode definition (`tools/src/tool_config.rs:17`):

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ToolEnvironmentMode {
    None,
    Single,
    Multiple,
}

impl ToolEnvironmentMode {
    pub fn from_count(count: usize) -> Self {
        match count {
            0 => Self::None,
            1 => Self::Single,
            _ => Self::Multiple,
        }
    }

    pub fn has_environment(self) -> bool {
        !matches!(self, Self::None)
    }
}
```

## Bounded proposed correction

Keep 0.164's `tool_environment_mode` implementation using the full configured
`environments.environments.len()`, including not-yet-ready attachments. Keep its
new shell schema/options and removed feature state. Do not revive
`StableEnvironmentTools` or restore ready-only environment counting.

`ToolEnvironmentMode::has_environment()` still exists and is true for Single
and Multiple, false for None. Add that predicate only at the four registration
sites whose old environment guard was removed:

```diff
--- frozen-0.164/core/src/tools/spec_plan.rs
+++ proposed/core/src/tools/spec_plan.rs
@@ add_shell_tools
-    if !features.enabled(Feature::ShellTool)
+    if !environment_mode.has_environment()
+        || !features.enabled(Feature::ShellTool)
@@ add_core_utility_tools: request permissions
-    if features.enabled(Feature::RequestPermissionsTool) {
+    if environment_mode.has_environment() && features.enabled(Feature::RequestPermissionsTool) {
@@ add_core_utility_tools: apply patch
-    if context.model_info.apply_patch_tool_type.is_some() {
+    if environment_mode.has_environment() && context.model_info.apply_patch_tool_type.is_some() {
@@ add_core_utility_tools: view image
-    if features.enabled(Feature::ViewImage) {
+    if environment_mode.has_environment() && features.enabled(Feature::ViewImage) {
```

These conditions omit the registrations, which removes both model advertisement
and native registry dispatch. They do not merely hide specs. For every nonempty
configured environment list the predicate is true, retaining 0.164's existing
registration, readiness handling and execution policy. Empty environments omit
ExecCommandHandler/WriteStdinHandler (or one-shot), RequestPermissionsHandler,
ApplyPatchHandler and ViewImageHandler. In the current fixed utility policy,
shell/view-image are already false; ApplyPatch is catalog-selected, and request
permissions can be inherited as enabled. Thus all four are proven affected
registration gates, with ApplyPatch the direct current-profile blocker.

No concrete additional registration gate change was established for
`incremental_tools`; its default promotion alone is not evidence of tool escape
and is outside this proposed correction. No catalog bytes, policy, public
protocol, enabled-environment tool behavior or provider choices change here.

Architect owns whether and how this proposal enters shared native packaging.
After any implementation, source/patch provenance, exact patched executable and
schemas must be refreshed; deterministic source checks cannot replace reviewed
both-profile empty-exposure and hostile-dispatch acceptance. Add source/unit
proof that empty environments omit both spec and handler, and that one/multiple
configured environments retain 0.164 behavior, including not-ready attachments.
Native campaigns remain deferred until final review.
