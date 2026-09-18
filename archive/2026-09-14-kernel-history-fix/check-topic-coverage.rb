require 'yaml'
require 'open3'

root = ARGV.fetch(0)
workflow = YAML.load_file(File.join(root, '.github/workflows/api-specs.yml'), aliases: true)
topics = workflow.fetch('jobs').fetch('api-specs-full').fetch('strategy').fetch('matrix').fetch('include')
script = <<~'BASH'
  set -euo pipefail
  shopt -s nullglob globstar
  files=()
  while IFS= read -r pat; do
    [[ -z "$pat" ]] && continue
    for f in $pat; do
      files+=("$f")
    done
  done <<< "$PATTERNS"
  (( ${#files[@]} > 0 ))
  printf '%s\n' "${files[@]}" | sort -u
BASH
counts = Hash.new(0)
topics.each do |topic|
  output, error, status = Open3.capture3({ 'PATTERNS' => topic.fetch('patterns') },
                                        'bash', '-c', script, chdir: File.join(root, 'api'))
  abort error unless status.success?
  output.lines.map(&:strip).each do |path|
    abort "Nonexistent spec: #{path}" unless File.file?(File.join(root, 'api', path))
    counts["api/#{path}"] += 1
  end
end
output, error, status = Open3.capture3('git', 'ls-files', 'api/spec/**/*_spec.rb',
                                    ':!api/spec/migrations/*_spec.rb', chdir: root)
abort error unless status.success?
tracked = output.lines.map(&:strip)
bad = (tracked | counts.keys).reject { |path| tracked.include?(path) && counts[path] == 1 }
abort bad.inspect unless bad.empty?
puts "Exact workflow shell expansion: #{tracked.size} tracked specs covered once; no nonexistent files"
