class LRU:
    def __init__(self):
        self.number_of_page_faults = 0

    def run(self, reference_string, number_of_frames):
        memory_state = []  # Represents the current state of memory
        page_last_used_at = {}  # Stores the last used time for each page in memory
        current_time = 0  # Keeps track of the 'time' for each page reference

        for page in reference_string:
            # If the page is not currently in memory, a page fault has occurred
            if page not in memory_state:
                # If the memory_state has space, add the page
                # Else, replace the 'oldest' page (the one not used for the longest time)
                if len(memory_state) < number_of_frames:
                    memory_state.append(page)
                else:
                    oldest_page = min(page_last_used_at, key=page_last_used_at.get)  # The page used the longest time ago
                    memory_state.remove(oldest_page)
                    memory_state.append(page)
                    del page_last_used_at[oldest_page]

                # Increase the count of page faults
                self.number_of_page_faults += 1

            # Whether the page is new or not, update its last used time
            page_last_used_at[page] = current_time
            current_time += 1

        return self.number_of_page_faults
