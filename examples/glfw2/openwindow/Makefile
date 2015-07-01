# to compile type make all
# to clean type make clean

OUT=glfw2_openwindow
DC=dmd
SRCS=openwindow.d
INCLUDES=-I../../../
# point this to wherever libglfw.so is ...
LIBS=-L`pkg-config --libs libglfw`
CLEAN=glfw2_openwindow.o glfw2_openwindow

all: ${SRCS}
	${DC} -of${OUT} ${INCLUDES} ${LIBS} $^

clean: ${CLEAN}
	-rm -f $^
.PHONY: clean
