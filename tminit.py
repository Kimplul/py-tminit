#!/usr/bin/python3
import usb.core

tm_wheel_infos = {
        0x0306: 0x0006, # T150RS
        0x0206: 0x0005, # T300RS
        0x0204: 0x0005, # T300 Ferrari Alcantara
        0x0002: 0x0002, # T500RS
        0x0407: 0x0001, # TMX
        }

def main():
    # Find the generic wheel
    dev = usb.core.find(idVendor = 0x44f, idProduct = 0xb65d)
    if dev is None:
        raise ValueError('Device not found')

    # Fetch the model number (along with some other cruft we don't know the
    # meaning of)
    dev_info = dev.ctrl_transfer(0xc1, 73, 0, 0, 0x10)
    if not dev_info:
        raise ValueError('Device did not respond')

    # Calculate the equivalent values as the ones used as keys in
    # tm_wheel_infos
    model_num = dev_info[6] + dev_info[7]*256

    # Start reboot sequence. Note that this WILL cause a USBError,
    # due to the nonstandard behaviour of the wheel.
    try:
        dev.ctrl_transfer(0x41, 83, tm_wheel_infos[model_num], 0, 0)
    except usb.core.USBError:
        # Pass, as this is unfortunately expected
        return

if __name__ == '__main__':
    main()
