# Installed selected Nix2.34.9 evidence

Documentation read from exact system-linked selected manual outputs; no Nix help command ran. Full file identities are in facts.json.

## Legacy instantiation

```text
The command \f(CRnix-instantiate\fR produces \fBstore derivation\fRs from (high-level) Nix expressions.
It evaluates the Nix expressions in each of \fIfiles\fR (which defaults to
\fI./default.nix\fR). Each top-level expression should evaluate to a
derivation, a list of derivations, or a set of derivations. The paths
of the resulting store derivations are printed on standard output.
.PP
If \fIfiles\fR is the character \f(CR-\fR, then a Nix expression will be read from

\f(CR--read-write-mode\fR
.IP
When used with \f(CR--eval\fR, perform evaluation in read/write mode so
nix language features that require it will still work (at the cost
of needing to do instantiation of every evaluated derivation). If
this option is not enabled, there may be uninstantiated store paths
in the final output.
```

## Modern eval option

```html
<p><span id="opt-read-only"><a href="#opt-read-only"><code>--read-only</code></a></span></p>
<p>Do not instantiate each evaluated derivation. This improves performance, but can cause errors when accessing store paths of derivations during evaluation.</p>
```

The legacy excerpt documents explicit materialization; it does not establish a supported --offline flag. The modern excerpt alone does not establish why the recorded original no-flag evaluation left no currently present za8/d0jj drv files. No cause or successful instantiation is inferred.
