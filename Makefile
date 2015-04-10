all::

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

.PHONY: all pgm-clean

.SECONDARY: recur recur/local.mak


