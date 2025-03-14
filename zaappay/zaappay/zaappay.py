"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

class State(rx.State):
  count: int = 0

  @rx.event
  def increment(self):
    self.count += 1

  @rx.event
  def decrement(self):
    print("hey")
    self.count -= 1


def index() -> rx.Component:
  return rx.container(
  rx.color_mode.button(position="top-right"),
  rx.center(rx.vstack(
  rx.heading("Welcome to ZaapPay!", size="9",color_scheme='green',font_family="Arial",font_weight="italic"),
  rx.text("Your One Step Platform all Payments",size='5'),
  rx.button("Get Started",on_click=State.decrement),
  rx.text(State.count),spacing="5",),
  spacing="5",justify="center",min_height="85vh",))


app = rx.App(
  theme=rx.theme(
  accent_color="green",
  radius="medium",
  color_scheme="light",))

app.add_page(index)
