# quick and dirty makefile to build the example
# I admit I don't know much about makefiles
# so if you can improve upon this by all means
# please do so; I can use the help :)

P:=glfw2_openwindow
DC:=dmd
SRCS:=openwindow.d
INCLUDES:=../../../
# point this to wherever libglfw.so is ...
LIBS:=`pkg-config --libs libglfw`

$(P): $(SRC)
	$(DC) -of$(P) -I$(INCLUDES) -L$(LIBS) $(SRCS)

clean:
	-rm -f glfw2_openwindow.o glfw2_openwindow
.PHONY: clean
