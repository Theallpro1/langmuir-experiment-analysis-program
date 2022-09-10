import tkinter as tk
import customtkinter as ctk

class Widget_Redrawer:
    def redraw_widgets(self, self_of_parent):
        self_of_parent.grid_columnconfigure(0,weight=1)
        self_of_parent.grid_columnconfigure(1,weight=1)
        self_of_parent.grid_rowconfigure(0,weight=1)

        self_of_parent.left_frame.grid(row=0, column = 0, sticky="nsew")
        self_of_parent.right_frame.grid(row=0, column = 1, sticky="nsew")

        self_of_parent.left_frame.grid_rowconfigure(0, weight = 7)
        self_of_parent.left_frame.grid_rowconfigure(1, weight = 1)
        self_of_parent.left_frame.grid_columnconfigure(0, weight = 1)

        self_of_parent.graph_frame.grid(row=0, column = 0, sticky = "nsew")
        self_of_parent.adding_frame.grid(row=1, column = 0, sticky = "nsew")

        self_of_parent.explorer_button.grid(row=0, column=0, sticky = "nsew")
        self_of_parent.deletion_button.grid(row=0, column=1, sticky = "nsew")
        self_of_parent.save_button.grid(row=0, column=2, sticky = "nsew")
        self_of_parent.zoom_button.grid(row=0, column=3, sticky = "nsew")
        self_of_parent.pan_button.grid(row=0, column=4, sticky = "nsew")
        self_of_parent.save_image_button.grid(row=0, column=5, sticky = "nsew")
        self_of_parent.trim_button.grid(row=0, column=6, sticky = "nsew")

        self_of_parent.right_frame.grid_columnconfigure(0, weight=1)
        self_of_parent.right_frame.grid_columnconfigure(1, weight=1)
        self_of_parent.right_frame.grid_rowconfigure(0, weight=1)
        self_of_parent.middle_frame.grid(row=0, column=0, sticky = "nswe")
        self_of_parent.middle_frame.grid_rowconfigure(0, weight = 1)
        self_of_parent.middle_frame.grid_rowconfigure(1, weight = 1)
        self_of_parent.selector_frame.grid(row=0, column=0, sticky = "nswe")
        self_of_parent.results_frame.grid(row=1, column=0, sticky = "nswe")
        self_of_parent.control_frame.grid(row=0, column=1, sticky = "nswe")

        self_of_parent.control_frame.grid_columnconfigure(0, weight=1)
        self_of_parent.control_frame.grid_rowconfigure(0, weight=1)
        self_of_parent.control_frame.grid_rowconfigure(1, weight=2)

        self_of_parent.options_frame.grid(row=0, column=0)
        self_of_parent.math_frame.grid(row=1, column=0)

        self_of_parent.select_all_frame.pack()
        self_of_parent.select_all_label.grid(row=0, column=0)
        self_of_parent.select_all_button.grid(row=0, column=1)

        self_of_parent.probe_area_frame.pack(fill = tk.X)
        self_of_parent.probe_area_label.grid(row = 0, column = 0)
        self_of_parent.probe_area_input.grid(row = 0, column = 1)
        self_of_parent.ion_mass_frame.pack(fill = tk.X)
        self_of_parent.ion_mass_label.grid(row = 0, column = 0)
        self_of_parent.ion_mass_input.grid(row = 0, column = 1)
        self_of_parent.temperature_frame.pack(fill=tk.X)
        self_of_parent.temperature_button.grid(row = 0, column = 0)
        self_of_parent.temperature_label.grid(row = 0, column = 1)
        self_of_parent.floating_frame.pack(fill=tk.X)
        self_of_parent.floating_potential_button.grid(row = 0, column = 0)
        self_of_parent.floating_label.grid(row = 0, column = 1)
        self_of_parent.debye_frame.pack(fill = tk.X)
        self_of_parent.debye_button.grid(row = 0, column = 0)
        self_of_parent.debye_label.grid(row = 0, column = 1)
        self_of_parent.debye_ratio_frame.pack(fill = tk.X)
        self_of_parent.debye_ratio_button.grid(row = 0, column = 0)
        self_of_parent.debye_ratio_label.grid(row = 0, column = 1)
        self_of_parent.basic_density_sef.put_on_screen()
        self_of_parent.probe_area_sef.put_on_screen()

        self_of_parent.scale_button.pack()
        self_of_parent.legend_button.pack()
        self_of_parent.rescale_button.pack()

        self_of_parent.derivative_button.pack()
        self_of_parent.box_button.pack()
        self_of_parent.average_button.pack()
        self_of_parent.basic_isat_button.pack()
        self_of_parent.basic_isat_button_auto.pack()
        self_of_parent.savgol_button.pack()
        self_of_parent.spline_button.pack()
        self_of_parent.eedf_button.pack()
        self_of_parent.plasma_potential_button.pack()
        self_of_parent.absolute_button.pack()
        self_of_parent.natural_log_button.pack()
        self_of_parent.square_button.pack()
        self_of_parent.oml_button.pack()

        self_of_parent.normal_plasma_potential_method_frame.pack()
        self_of_parent.potential_bounds_1_button.grid(row=0,column=0)
        self_of_parent.potential_bounds_1_label.grid(row=0,column=1)
        self_of_parent.potential_bounds_2_button.grid(row=1,column=0)
        self_of_parent.potential_bounds_2_label.grid(row=1,column=1)
        self_of_parent.normal_potential_button.grid(row=2,column=0)
        self_of_parent.normal_potential_label.grid(row=2,column=1)

        self_of_parent.cursor_frame.pack()
        self_of_parent.minus_button_l.grid(row=0,column=0)
        self_of_parent.minus_button.grid(row=0,column=1)
        self_of_parent.plus_button.grid(row=0,column=3)
        self_of_parent.plus_button_l.grid(row=0,column=4)
        self_of_parent.fit_counter.grid(row=0,column=2)
        self_of_parent.cursor_show_button.grid(row=0,column=5)
        self_of_parent.minus_button_l_2.grid(row=1,column=0)
        self_of_parent.minus_button_2.grid(row=1,column=1)
        self_of_parent.plus_button_2.grid(row=1,column=3)
        self_of_parent.plus_button_l_2.grid(row=1,column=4)
        self_of_parent.fit_counter_2.grid(row=1,column=2)
        self_of_parent.cursor_show_button_2.grid(row=1,column=5)

        self_of_parent.open_help_and_options_button.pack()
