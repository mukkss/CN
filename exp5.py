import random
import time

# Initialize variables
window_size = int(input("Enter the window size: "))
total_frames = int(input("Enter the total number of frames to be sent: "))
send_base = 0
next_seq_num = 0
acknowledged = [False] * total_frames


# Function to simulate sending a frame
def send_frame(frame_number):
    print(f"Sending frame {frame_number}")


# Function to simulate receiving an acknowledgment with random loss
def receive_ack():
    # 90% chance of successful acknowledgment
    if random.randint(0, 99) < 90:
        ack_frame = send_base + random.randint(0, window_size - 1)
        print(f"Acknowledgment received for frame {ack_frame}")
        return ack_frame
    else:
        print("Acknowledgment lost!")
        return -1  # No acknowledgment received


# Function to slide the window when an ACK is received
def slide_window(ack_frame):
    global send_base
    while send_base <= ack_frame < total_frames:
        acknowledged[send_base] = True
        print(f"Frame {send_base} acknowledged.")
        send_base += 1


# Main function to run the sliding window protocol
def run_sliding_window():
    global next_seq_num
    while send_base < total_frames:
        # Send frames within the window
        while next_seq_num < send_base + window_size and next_seq_num < total_frames:
            send_frame(next_seq_num)
            next_seq_num += 1

        # Simulate receiving an acknowledgment
        ack_frame = receive_ack()
        if ack_frame != -1:
            slide_window(ack_frame)
        else:
            print("Timeout! Resending frames...")
            next_seq_num = send_base  # Restart sending from the unacknowledged base frame

        # Simulate delay
        time.sleep(1)

def main():# Run the protocol
    run_sliding_window()

if __name__ == "__main__":
    main()
