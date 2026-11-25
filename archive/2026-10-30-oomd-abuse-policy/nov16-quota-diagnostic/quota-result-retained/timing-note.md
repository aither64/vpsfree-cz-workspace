# Retained timing clarification

Root's terminal handoff records the early watcher overrun assertion as incorrect:
it was made 7m34s after registration. This does not alter the original watcher
statement or immutable operation evidence. Native receipt timing is authoritative:
982.9220189s for the script and982.6382171s for the ordinary command. Native
runner log additionally records721.53s for the default script and268.74s for its
single example; these are nested clocks and are not summed. The result is a
successful non-reproduction, with the historical failure retained separately.
