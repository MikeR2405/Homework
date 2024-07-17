import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game'


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('bal.png', 0.02)
        self.change_x = 4
        self.change_y = 4

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.5)
        self.change_x = 0

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.score = 0
        self.game_over = False
        # Добавляем переменную цвета подложки
        self.background_color = arcade.color.WHITE
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear(self.background_color)  # используем переменную подложки
        self.bar.draw()
        self.ball.draw()
        arcade.draw_text(f'Score: {self.score}', 10, SCREEN_HEIGHT - 20, arcade.color.BLACK, 14)
        arcade.draw_text('сделано by MikeR', SCREEN_WIDTH / 2, SCREEN_HEIGHT - 20, arcade.color.BLACK, 14, anchor_x="center")  # Добавляем текст по центру

        if self.game_over:
            arcade.draw_text('Game Over', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.ALMOND, 50, bold=True)

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y

        self.ball.update()
        self.bar.update()

        if self.ball.bottom <= 0:
            self.score += 1
            self.ball.center_x = SCREEN_WIDTH / 2
            self.ball.center_y = SCREEN_HEIGHT / 2
        #    Если счет достигает значения -> меняем цвет подложки, показываем надпись и игра закрывается
        if self.score >= 4:
            self.game_over = True
            self.background_color = arcade.color.ALABAMA_CRIMSON
            arcade.schedule(self.close_game, 10)

    def close_game(self, delta_time):
        arcade.close_window()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 4
        if key == arcade.key.LEFT:
            self.bar.change_x = -4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
