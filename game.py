import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Hexagon")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ball properties
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_vx = 5  # Initial x velocity
ball_vy = 5  # Initial y velocity
ball_color = RED

# Hexagon properties
hexagon_center_x = WIDTH // 2
hexagon_center_y = HEIGHT // 2
hexagon_side_length = 100
hexagon_color = WHITE

def calculate_hexagon_vertices(center_x, center_y, side_length):
    """Calculates the vertices of a hexagon."""
    vertices = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = math.radians(angle_deg)
        x = center_x + side_length * math.cos(angle_rad)
        y = center_y + side_length * math.sin(angle_rad)
        vertices.append((x, y))
    return vertices

hexagon_vertices = calculate_hexagon_vertices(
    hexagon_center_x, hexagon_center_y, hexagon_side_length
)

def distance(x1, y1, x2, y2):
    """Calculates the distance between two points."""
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def check_collision(ball_x, ball_y, ball_radius, v1x, v1y, v2x, v2y):
    """Checks for collision between the ball and a line segment."""
    # Calculate the distance from the ball to the line
    dx = v2x - v1x
    dy = v2y - v1y
    a = dx**2 + dy**2
    if a == 0:
        return False, 0, 0  # Line is just a point

    # Calculate the parameter t, which represents the position of the closest
    # point on the line to the ball.
    t = ((ball_x - v1x) * dx + (ball_y - v1y) * dy) / a

    # If t is not within the range [0, 1], the closest point is outside the
    # line segment.
    if t < 0:
        closest_x = v1x
        closest_y = v1y
    elif t > 1:
        closest_x = v2x
        closest_y = v2y
    else:
        closest_x = v1x + t * dx
        closest_y = v1y + t * dy

    # Calculate the distance from the ball to the closest point on the line
    dist = distance(ball_x, ball_y, closest_x, closest_y)

    if dist <= ball_radius:
        # Collision occurred!
        return True, closest_x, closest_y
    else:
        return False, 0, 0

def reflect_velocity(ball_x, ball_y, ball_vx, ball_vy, line_x1, line_y1, line_x2, line_y2):
    """Reflects the ball's velocity based on the collision with a line."""
    # Calculate the normal vector to the line
    normal_x = line_y2 - line_y1
    normal_y = -(line_x2 - line_x1)

    # Normalize the normal vector
    norm_length = math.sqrt(normal_x**2 + normal_y**2)
    if norm_length == 0:
        return ball_vx, ball_vy  # Avoid division by zero

    normal_x /= norm_length
    normal_y /= norm_length

    # Calculate the dot product of the velocity vector and the normal vector
    dot_product = ball_vx * normal_x + ball_vy * normal_y

    # Calculate the reflection vector
    reflected_vx = ball_vx - 2 * dot_product * normal_x
    reflected_vy = ball_vy - 2 * dot_product * normal_y

    return reflected_vx, reflected_vy

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_x += ball_vx
    ball_y += ball_vy

    # Collision detection with hexagon edges
    for i in range(6):
        v1x, v1y = hexagon_vertices[i]
        v2x, v2y = hexagon_vertices[(i + 1) % 6]  # Next vertex (loop around)

        collided, _, _ = check_collision(ball_x, ball_y, ball_radius, v1x, v1y, v2x, v2y)

        if collided:
            ball_vx, ball_vy = reflect_velocity(ball_x, ball_y, ball_vx, ball_vy, v1x, v1y, v2x, v2y)
            # Small adjustment to move the ball out of the collision
            ball_x += ball_vx
            ball_y += ball_vy
            break  # Only reflect once per frame

    # Keep ball within screen bounds (optional, but prevents getting stuck)
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_vx *= -1
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_vy *= -1

    # Drawing
    screen.fill(BLACK)  # Clear the screen
    pygame.draw.polygon(screen, hexagon_color, hexagon_vertices)
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
