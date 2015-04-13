all::

NL_CORPUS = corpus/pan15-authorship-verification-training-dataset-dutch-2015-03-02
EN_CORPUS = corpus/pan15-authorship-verification-training-dataset-english-2015-03-02
ES_CORPUS = corpus/pan15-authorship-verification-training-dataset-spanish-2015-03-02
GR_CORPUS = corpus/pan15-authorship-verification-training-dataset-greek-2015-03-02

recur:
	git clone https://github.com/douglasbagnall/recur.git

recur/local.mak: recur
	cp $@.example.x86_64 $@

recur/charmodel.so: recur/local.mak
	cd recur && git pull
	cd recur && make charmodel.so

charmodel.so: recur/charmodel.so
	ln -s $^ $@

pgm-clean:
	rm -rf images
	mkdir images

pyc-clean:
	rm -f *.pyc mappings/*.pyc

.PHONY: all pgm-clean all-mappings

.SECONDARY: recur recur/local.mak

mappings/nl.py:
	./corpus-utils -m $(NL_CORPUS) -d --decompose-caps > $@

mappings/en.py:
	./corpus-utils -m $(EN_CORPUS) -d --decompose-caps > $@

mappings/es.py:
	./corpus-utils -m $(ES_CORPUS) -d --decompose-caps > $@

mappings/gr.py:
	./corpus-utils -m $(GR_CORPUS) -d --decompose-caps --collapse-latin > $@

all-mappings: mappings/gr.py mappings/en.py  mappings/es.py mappings/nl.py
