import time


# This first function is very simple. It basically returns the division of the provided numbers except when d is 0
def division_possible_zero(n, d):
    return (n / d) if d else 0


# This class provides timer functionalities to any script that requires it.
# It provides with basic elapsed time functionality, with associated
# print functionality of the elapsed time, as well as more advanced
# progress management functionalities with its associated print functionality
class Timer:

    # To first define the timer we do not need to provide anything since the class
    # will automatically store the time at which it has been initialized
    def __init__(self):
        self.start_time = time.time()
        self.elapsed_time = 0  # We also initialize other necessary variables
        self.elapsed_time_precise = 0
        self.completion_percentage = 0
        self.estimated_time = 0
        self.progress_string = ''
        self.elapsed_time_string = ''
        self.elapsed_time_precise_string = ''

    # This method updates the elapse_time variable that takes the current time
    # (time.time()) and this is subtracted from the start_time
    def update_elapsed_time(self, kronos=False, print_elapsed_time=False, precise_time=False):
        # Calculate the elapsed time with and without that much precision
        self.elapsed_time_precise = (time.time() - self.start_time)
        self.elapsed_time = int(round((time.time() - self.start_time)))

        if kronos and print_elapsed_time:
            if precise_time:
                self.elapsed_time_precise_string = ('Elapsed time: ' + str('{0:.6f}'.format(
                    self.elapsed_time_precise / 8640) + ' kr. '))
                # Print time in micronos (1000=8.6s) for easier elapsed time management
                print(self.elapsed_time_precise_string)
            else:
                self.elapsed_time_string = ('Elapsed time: ' + str('{0:.3f}'.format(
                    self.elapsed_time_precise / 8640)) + ' kr. ')
                # Print time in milikronos (1=8.6s) for easier elapsed time management
                print(self.elapsed_time_string)

        elif not kronos and print_elapsed_time:
            if precise_time:
                self.elapsed_time_precise_string = ('Elapsed time: ' + str('{0:.6f}'.format(
                    self.elapsed_time_precise) + ' kr. '))
                print(self.elapsed_time_precise_string)
            else:
                self.elapsed_time_string = ('Elapsed time: ' + str(self.elapsed_time) + ' s. ')
                print(self.elapsed_time_string)

    # This method more accurately tracks progress with both the steps
    # and the time information it calculates the estimated time as well as the completion percentage
    # and it prints everything on the bash for further timekeeping purposes
    def update_progress(self, current_step, total_steps, print_progress=False, kronos=False):
        self.elapsed_time = int(round((time.time() - self.start_time)))
        self.completion_percentage = round((division_possible_zero(current_step, total_steps)) * 100, 2)
        self.estimated_time = int(
            round(division_possible_zero((100 * self.elapsed_time), self.completion_percentage), 0))

        if print_progress:
            if kronos:
                self.progress_string = (str('{0:.2f}'.format(self.completion_percentage)) + ' % Elapsed time: ' + str(
                    '{0:.3f}'.format(self.elapsed_time / 8640)) + ' kr, Estimated time: ' + str('{0:.3f}'.format(
                    self.estimated_time / 8640)) + ' kr. ')
                print(self.progress_string)

            else:
                self.progress_string = (str('{0:.2f}'.format(self.completion_percentage)) + ' % Elapsed time: ' + str(
                    self.elapsed_time) + ' s, Estimated time: ' + str(
                    self.estimated_time) + ' s. ')  # We also provide print functionality for easier progress management
                print(self.progress_string)