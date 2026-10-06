require File.expand_path('spec/spec_helper', Dir.pwd)
RSpec.configure do |config|
  config.before(:suite) do
    report = proc do |ret, context, error|
      message = error.message.gsub(/(token|password|secret)=\S+/i, '\\1=[REDACTED]')
      warn "EXCEPTION PROBE #{error.class}: #{message}"
      warn error.backtrace.first(10).join("\n")
      ret
    end
    HaveAPI::Action.connect_hook(:exec_exception, &report)
    VpsAdmin::API.default.connect_hook(:request_exception, &report)
  end
end
RSpec.configure do |config|
  config.around do |example|
    if example.full_description.include?('MetricsAccessToken Create ignores user selection')
      trace = TracePoint.new(:raise) do |event|
        error = event.raised_exception
        next if error.is_a?(NoMethodError) && error.name == :obj_type
        warn "RAISE PROBE #{error.class}: #{error.message}"
        warn error.backtrace.first(8).join("\n")
      end
      trace.enable { example.run }
    else
      example.run
    end
  end
end
