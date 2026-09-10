# frozen_string_literal: true

require 'fileutils'
require 'json'
require 'minitest/autorun'
require 'open3'
require 'rbconfig'
require 'tmpdir'

class DeploymentContractTest < Minitest::Test
  CHECKER = File.expand_path('../bin/check-dev-workspace-deployment', __dir__)
  REVISION = 'a' * 40

  def test_matching_site_and_runtime_pass
    with_contract do |workspace, configuration, environment|
      output, error, status = Open3.capture3(
        environment, CHECKER, '--workspace-root', workspace,
        '--configuration-root', configuration
      )

      assert(status.success?, error)
      assert_includes(output, REVISION)
    end
  end

  def test_site_or_runtime_drift_fails
    with_contract do |workspace, configuration, environment|
      File.write(
        File.join(workspace, '.dev-workspace.json'),
        JSON.generate(workspace_config('different.example.test'))
      )
      _output, error, status = Open3.capture3(
        environment, CHECKER, '--workspace-root', workspace,
        '--configuration-root', configuration
      )
      refute(status.success?)
      assert_includes(error, 'portal identity differ')

      File.write(
        File.join(workspace, '.dev-workspace.json'),
        JSON.generate(workspace_config('site.workspace.example.test'))
      )
      write_lock(File.join(configuration, 'flake.lock'), root_input: 'devWorkspace', revision: 'b' * 40)
      _output, error, status = Open3.capture3(
        environment, CHECKER, '--workspace-root', workspace,
        '--configuration-root', configuration
      )
      refute(status.success?)
      assert_includes(error, 'different generic runtimes')
    end
  end

  def test_non_object_workspace_configuration_fails_without_a_traceback
    with_contract do |workspace, configuration, environment|
      File.write(File.join(workspace, '.dev-workspace.json'), "[]\n")
      _output, error, status = Open3.capture3(
        environment, CHECKER, '--workspace-root', workspace,
        '--configuration-root', configuration
      )

      refute(status.success?)
      assert_includes(error, 'workspace registration or aitherdev portal identity is malformed')
      refute_includes(error, CHECKER)
    end
  end

  private

  def with_contract
    Dir.mktmpdir('dev-workspace-contract-test') do |directory|
      workspace = File.join(directory, 'workspace')
      configuration = File.join(directory, 'configuration')
      FileUtils.mkdir_p(workspace)
      site_directory = File.join(configuration, 'cluster/cz.vpsfree/machines/aitherdev')
      FileUtils.mkdir_p(site_directory)
      File.write(
        File.join(workspace, '.dev-workspace.json'),
        JSON.generate(workspace_config('site.workspace.example.test'))
      )
      write_workspace_lock(File.join(workspace, 'flake.lock'))
      write_lock(File.join(configuration, 'flake.lock'), root_input: 'devWorkspace', revision: REVISION)
      File.write(File.join(site_directory, 'dev-workspace-site.nix'), "{ }\n")
      nix = File.join(directory, 'nix')
      File.write(nix, "#!#{RbConfig.ruby}\nputs #{JSON.generate(site_config).inspect}\n")
      File.chmod(0o755, nix)
      yield workspace, configuration, { 'NIX_COMMAND' => nix }
    end
  end

  def workspace_config(hostname)
    {
      'schema' => 2,
      'portal' => {
        'hostname' => hostname,
        'aliases' => ['legacy.example.test']
      }
    }
  end

  def site_config
    {
      'hostName' => 'site.workspace.example.test',
      'wildcardHost' => '*.workspace.example.test',
      'aliases' => ['legacy.example.test']
    }
  end

  def write_workspace_lock(path)
    File.write(path, JSON.generate(
      'root' => 'root',
      'nodes' => {
        'root' => { 'inputs' => { 'vpsfree-dev-workspace' => 'organization' } },
        'organization' => { 'inputs' => { 'dev-workspace' => 'generic' } },
        'generic' => { 'locked' => locked(REVISION) }
      }
    ))
  end

  def write_lock(path, root_input:, revision:)
    File.write(path, JSON.generate(
      'root' => 'root',
      'nodes' => {
        'root' => { 'inputs' => { root_input => 'generic' } },
        'generic' => { 'locked' => locked(revision) }
      }
    ))
  end

  def locked(revision)
    {
      'type' => 'github', 'owner' => 'aither64',
      'repo' => 'dev-workspace', 'rev' => revision
    }
  end
end
