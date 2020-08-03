from src import controller
import pygame

def main():
    pygame.init()
    print("Software Lead is: Ron Laniado")
    print("Backend is: David Esses")
    print("Frontend is: Matthew Sadowski")
    window = controller.Controller()
    window.mainLoop()
main()
