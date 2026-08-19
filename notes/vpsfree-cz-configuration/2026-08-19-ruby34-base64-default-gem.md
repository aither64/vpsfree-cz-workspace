# Ruby 3.4 XARF Base64 decoding

Related initiative: work/2026-08-19-abusix-reports

## Symptom

Focused parser specs failed while loading the base64 library:

    cannot load such file -- base64

## Cause

The repository's Ruby 3.4 development shell does not include base64 as a
default gem.

## Workaround

For strict Base64 decoding without adding a dependency, use Ruby's built-in
String#unpack1('m0'). The m0 directive rejects malformed input with
ArgumentError, unlike permissive decoding modes.

## Verification

The XARF decoder specifications cover valid and malformed Base64. The focused
suite passed with 24 examples, and the full repository suite passed with 36
examples.
