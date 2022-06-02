#Makefile
  
all: raidix

raidix: main.o task.o 
	cc -o raidix main.o task.o

main.o: main.c
	cc -c main.c

task.o: task.c
	cc -c task.c

clean:
	rm ./*.o
install:
	cp raidix /usr/bin/

