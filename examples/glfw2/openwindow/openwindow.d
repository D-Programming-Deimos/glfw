import deimos.glfw.glfw2;
/*
  arshok:
    open a window at 320 x 240 px resolution using default depths.
    sleep for 3 seconds then destroy the window and exit.
*/
void main() {

  glfwInit();
  glfwOpenWindow(320,240, 0,0,0,0,0,0, GLFW_WINDOW);
  glfwSleep(3);
  glfwCloseWindow();
  glfwTerminate();

}
