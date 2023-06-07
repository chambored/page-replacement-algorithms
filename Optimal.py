class Optimal:
    def __init__(self):
        self.number_of_page_faults = 0

    def run(self, reference_string, number_of_frames):
        memory_state = []  # Represents the current state of memory

        # Iterate over the reference_string
        for i in range(len(reference_string)):
            # If memory_state is not full and page is not in memory_state, add the page to memory_state
            if len(memory_state) < number_of_frames and reference_string[i] not in memory_state:
                memory_state.append(reference_string[i])
                self.number_of_page_faults += 1

            # Else if page is not in memory_state and memory_state is full, replace the farthest page in future reference with the current page
            elif len(memory_state) == number_of_frames and reference_string[i] not in memory_state:
                # Find the farthest page in future reference
                farthest_distance_in_future = 0
                index_of_farthest_page = 0
                for page_in_memory in memory_state:
                    try:
                        distance_in_future = reference_string[i:].index(page_in_memory)
                    except ValueError:
                        distance_in_future = float('inf')  # The page_in_memory is not in the rest of the reference_string

                    if distance_in_future > farthest_distance_in_future:
                        farthest_distance_in_future = distance_in_future
                        index_of_farthest_page = memory_state.index(page_in_memory)

                memory_state[index_of_farthest_page] = reference_string[i]
                self.number_of_page_faults += 1

            # Else the page is already in memory_state, so do nothing

        return self.number_of_page_faults
