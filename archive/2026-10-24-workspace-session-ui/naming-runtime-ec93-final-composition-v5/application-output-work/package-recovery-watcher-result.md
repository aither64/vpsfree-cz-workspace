The assigned operation did not start. Passing the JSON object unchanged to `subprocess.run` failed because it uses the key `cmd`, which `Popen` does not accept. No recovery process or output directory was created.

I stopped without retrying, as instructed. The exact failure was `TypeError: Popen.__init__() got an unexpected keyword argument 'cmd'`.