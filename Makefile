OUT = tmuxline-16dark.conf tmuxline-16light.conf tmuxline-256dark.conf tmuxline-256light.conf tmuxline-16Mdark.conf tmuxline-16Mlight.conf
PYTHON = python

all: $(OUT)

tmuxline-16dark.conf: tmuxline-dark.in transform.py
	$(PYTHON) transform.py 16 $< $@

tmuxline-16light.conf: tmuxline-light.in transform.py
	$(PYTHON) transform.py 16 $< $@

tmuxline-256dark.conf: tmuxline-dark.in transform.py
	$(PYTHON) transform.py 256 $< $@

tmuxline-256light.conf: tmuxline-light.in transform.py
	$(PYTHON) transform.py 256 $< $@

tmuxline-16Mdark.conf: tmuxline-dark.in transform.py
	$(PYTHON) transform.py 16M $< $@

tmuxline-16Mlight.conf: tmuxline-light.in transform.py
	$(PYTHON) transform.py 16M $< $@

clean:
	rm $(OUT)

.PHONY: all clean
