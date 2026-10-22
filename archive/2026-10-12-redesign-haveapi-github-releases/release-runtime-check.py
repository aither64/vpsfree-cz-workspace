import subprocess


def git(*args):
    return subprocess.check_output(['git', *args])


paths = [
    'servers/ruby/lib', 'clients/ruby/lib', 'clients/go/lib',
    'clients/js/src', 'clients/php/src',
]
versions = {
    'servers/ruby/lib/haveapi/version.rb',
    'clients/ruby/lib/haveapi/client/version.rb',
    'clients/go/lib/haveapi/go_client/version.rb',
    'clients/js/src/haveapi/client.js',
    'clients/php/src/Client.php',
}
changed = set(git('diff', '--name-only', 'v0.29.9', 'HEAD', '--', *paths).decode().splitlines())
assert changed == versions, changed
for path in versions:
    before = git('show', f'v0.29.9:{path}')
    after = git('show', f'HEAD:{path}')
    assert before.replace(b'0.29.9', git('show', 'HEAD:VERSION').strip()) == after, path
assert not git('diff', 'v0.29.9', 'HEAD', '--', 'servers/elixir', 'clients/elixir')
assert not git('diff', 'v0.29.9', 'HEAD', '--', 'servers/ruby/spec', 'clients/ruby/spec',
               'clients/go/spec', 'clients/js/test', 'clients/php/tests')
print('Runtime sources preserve 0.29.9 behavior; existing tests and Elixir unchanged')
