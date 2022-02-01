
import os
sysfs_path = '/sys/class/gpio'
sysfs_export_path=f'{sysfs_path}/export'
sysfs_unexport_path=f'{sysfs_path}/export'
sysfs_gpio_path=f'{sysfs_path}/gpio%d'
sysfs_gpio_direction=f'{sysfs_gpio_path}/direction'
sysfs_gpio_value=f'{sysfs_gpio_path}/value'
input='in'
output='out'
low_value='0'
high_value='1'
available_gpio_pins = [18,19,20,21,22,23,23,24,25,26]
allocated_gpio_pins = []
class GPIO():
    def __init__(self,pin_number,direction):
        self.pin_number=pin_number
        self.direction=direction
        self.pin_dir_path = sysfs_gpio_direction % self.pin_number
        self.pin_path = sysfs_gpio_path % self.pin_number
        self.pin_value_path=sysfs_gpio_value % self.pin_number
        self.is_pin_available(self.pin_number)
        self.create_pin()
        self.get_permission()
        self.set_pin_direction()
        self.value_file = open(self.pin_value_path, 'r+')
        allocated_gpio_pins.append(self.pin_number)


    def create_pin(self):
        if not os.path.isdir(self.pin_path):
            with open(sysfs_export_path,'w') as file:
                file.write('%d' % self.pin_number)


    def get_permission(self):
        try:
            os.system(f"chmod 775 {self.pin_dir_path}")
        except Exception as e:
            print(f'{e.__str__()}')

    def set_pin_direction(self):
        with open(self.pin_dir_path, 'w') as file:
            file.write(self.direction)
       
    def low(self):
        self.value_file.write(low_value)
        self.value_file.seek(0)

    def high(self):
        self.value_file.write(high_value)
        self.value_file.seek(0)

    #def set_value(self):

    def get_value(self):
        val = self.value_file.read()
        self.value_file.seek(0)
        return int(val)

    def is_pin_available(self, number):
        if number not in available_gpio_pins:
            raise Exception("Pin number out of range")

        if number in allocated_gpio_pins:
            raise Exception("Pin already allocated")
