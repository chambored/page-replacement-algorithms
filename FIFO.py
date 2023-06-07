class FIFO:
    def __init__(self):
        self.number_of_page_faults = 0

    def run(self, reference_string, number_of_frames):
        memory_state = []  # This represents the current state of memory holding the pages

        for page in reference_string:
            # If the page is not in memory, a page fault has occurred
            if page not in memory_state:
                # If the memory_state size is less than the number of frames, add the page to memory_state
                # else remove the first (oldest) page in memory_state and add the new page at the end
                if len(memory_state) < number_of_frames:
                    memory_state.append(page)
                else:
                    memory_state.pop(0)
                    memory_state.append(page)

                # Increase the count of page faults
                self.number_of_page_faults += 1
            # else, the page is already in memory_state, so no page fault, thus do nothing

        return self.number_of_page_faults
