import user_interface as ui
import data_record as dr
import data_export as de


def run():
    selection = ui.welcome_screen()
    if selection == 1:
        dr.make_a_record()
    else:
        de.export_from_file()
