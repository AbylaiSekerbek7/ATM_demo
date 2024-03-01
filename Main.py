import pygame
from Button import Button

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ATM SIMULATOR")
clock = pygame.time.Clock()
Fps = 60

#settings
koshelek = 0
bank_balance = 0
deposit = 0

#  images
bg = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
btn_width, btn_height = 200, 60

vnesty_btn_img = pygame.image.load("images/vnesty.png")
vnesty_btn_img = pygame.transform.scale(vnesty_btn_img , (btn_width, btn_height))
rabotat_btn_img = pygame.image.load("images/rabotat.png")
bankomat_btn_img = pygame.image.load("images/bankomat.png")
snyatt_btn_img = pygame.image.load("images/snyatt.png")
back_btn_img = pygame.image.load("images/back.png")



#buttons
vnesty_button = Button(WIDTH//2+50, HEIGHT-200, vnesty_btn_img, 1)
snyatt_button = Button(WIDTH//2-250, HEIGHT-200, snyatt_btn_img,1.1)
rabotat_button = Button(WIDTH//2, HEIGHT // 2, rabotat_btn_img, 1)
bankomat_button = Button(WIDTH//2 - 300, HEIGHT//2, bankomat_btn_img,1)
back_button = Button(20, HEIGHT-100, back_btn_img,0.1)

# Fonts

font_1 = pygame.font.SysFont('Futura', 100, False, False)
font_2 = pygame.font.SysFont('Futura', 40, False, False)
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

is_taking_money = False
is_menu = True
running = True
# Initialize employee data
days_worked = 0
salary_per_day = 50  # Adjust the salary as needed

while running:
    screen.fill((255,255,255))
    #screen.blit(bg,(0, 0))
    if is_menu:
        draw_text("ATM SIMULATOR", font_1, (0, 0, 0), WIDTH // 2 - 280, 60)
        draw_text(f"Баланс: {money}", font_2, (0, 0, 0), 10, 10)

        if rabotat_button.draw(screen):
            days_worked += 1
            koshelek += salary_per_day
            print(f"Employee worked {days_worked} days. Salary added: ${salary_per_day}")

        if bankomat_button.draw(screen):
            is_menu = False
    else:
        draw_text("ATM", font_1, (0, 0, 0), WIDTH // 2 - 100, 60)
        draw_text(f"Balance: {bank_balance}", font_2, (0, 0, 0), 10, 10)

        if vnesty_button.draw(screen):
            # Ask for deposit amount
            deposit_amount = float(input("Enter the amount to deposit: "))
            bank_balance += deposit_amount
            print(f"Deposited ${deposit_amount}. New balance: ${bank_balance}")

        if snyatt_button.draw(screen):
            # Ask for withdrawal amount
            withdrawal_amount = float(input("Enter the amount to withdraw: "))
            if withdrawal_amount <= bank_balance:
                bank_balance -= withdrawal_amount
                print(f"Withdrew ${withdrawal_amount}. New balance: ${bank_balance}")
            else:
                print("Insufficient funds!")

        if back_button.draw(screen):
            is_menu = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()