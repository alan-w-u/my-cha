from gpiozero import Servo, Motor
from time import sleep

powder_servo_pin = 17
water_servo_pin = 27
pump_motor_forward_pin = 23
pump_motor_backward_pin = 24
whisk_motor_forward_pin = 25
whisk_motor_backward_pin = 8

powder_servo = Servo(powder_servo_pin)
water_servo = Servo(water_servo_pin)
pump_motor = Motor(forward=pump_motor_forward_pin, backward=pump_motor_backward_pin)
whisk_motor = Motor(forward=whisk_motor_forward_pin, backward=whisk_motor_backward_pin)

def setup():
  powder_servo.min()
  water_servo.min()
  sleep(1)
  powder_servo.detach()
  water_servo.detach()

def make_matcha(intensity, size):
  # Pour matcha powder
  powder_servo.value = 0.5

  match intensity:
    case "Mild":
      sleep(0.5)
    case "Regular":
      sleep(1)
    case "Strong":
      sleep(1.5)
  
  powder_servo.min()
  powder_servo.detach()

  # Pour water
  pump_motor.forward()

  match size:
    case "Small":
      sleep(30)
    case "Medium":
      sleep(60)
    case "Large":
      sleep(90)
  
  pump_motor.stop()

  # Whisk
  whisk_motor.forward()
  sleep(30)
  whisk_motor.stop()

  # Pour matcha
  water_servo.max()
  sleep(1)
