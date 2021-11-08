import pygame
#import ray
import math

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
FPS = 60
PARTICLES = 20000 
PARTICLES_PER_RING = 1000
RADIUS_OF_INNER = 100
DIS_BT_RINGS = 10
FRAMES = 100
G_CONST = 1
MIN_DIST = 50
DT=.1
def drawCircle(circle):
    pygame.draw.circle(screen, RED, circle, 1)
    

def draw_window(positions, frame):
    screen.fill(WHITE)
    for circle in positions[frame]:
        drawCircle(circle)
    pygame.display.update()

def render(positions):
    clock = pygame.time.Clock()
    run = True
    while run:
        for frame in range(FRAMES):
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            draw_window(positions, frame)

    pygame.quit()

def initialize():
    positions = []
    positions.append(((WIDTH/2, HEIGHT/2), (0, 0), 10000))
    for index in range(PARTICLES):
        r = RADIUS_OF_INNER+(math.floor(index/PARTICLES_PER_RING))*DIS_BT_RINGS
        ang = index * math.pi * 2 / PARTICLES_PER_RING
        px = .4*r*math.cos(ang) + WIDTH/2
        py = r*math.sin(ang) + HEIGHT/2
        S = 20#-5*math.floor(index/PARTICLES_PER_RING)
        vx = -math.sin(ang) * S
        vy = math.cos(ang) * S
        positions.append(((px, py), (vx, vy), 100))
    return positions

def extract_positions(frame):
    positions = []
    for i in frame:
        positions.append(i[0])
    return positions


def calculate_new_frame(previous_frame):
    new_frame = []
    for particle_index in range(len(previous_frame)):
        current_particle = previous_frame[particle_index]
        new_vx = current_particle[1][0]
        new_vy = current_particle[1][1]
        # for each_particle_index in range(len(previous_frame)):
        for each_particle_index in range(1):
            each_particle = previous_frame[each_particle_index]
            if each_particle_index != particle_index:
                dx = each_particle[0][0] - current_particle[0][0]
                dy = each_particle[0][1] - current_particle[0][1]
                dx_sq = dx * dx
                dy_sq = dy * dy
                m = (dy_sq+dx_sq)**(1/2)
                ax = G_CONST*each_particle[2]/(dx_sq+100)
                ay = G_CONST*each_particle[2]/(dy_sq+100)
                new_vx += dx/m *ax* DT
                new_vy += dy/m *ay* DT
        new_particle = ((new_vx*DT+current_particle[0][0], new_vy*DT+current_particle[0][1]), (new_vx,new_vy), current_particle[2])
        new_frame.append(new_particle)
    return new_frame

                
                
        

def calculate():
    frames = []
    previous_frame = initialize()
    first_frame = extract_positions(previous_frame)

    frames.append(first_frame)
    
    for frame in range(FRAMES):
        new_frame = calculate_new_frame(previous_frame)

        frames.append(extract_positions(new_frame))
        previous_frame = new_frame
        print(frame)

    return frames

def main():
    positions = calculate()
    render(positions)

if __name__ == "__main__":
    main()