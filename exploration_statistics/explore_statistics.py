import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

base_dir = '/home/xiaoyang/test_ws/data/explore_statistics/range_5'

def read_and_interpolate_csv(file_path, common_time, x_col, y_col):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Interpolate the y_col to the common time points
    interpolated_values = np.interp(common_time, df[x_col], df[y_col])
    
    return interpolated_values

def main():
    total_voxel = 1000 *26.4 * 41.4 * 2
    total_view_angle = 8 * 8

    # Get the list of experiment folders
    experiment_folders = [f for f in glob.glob(os.path.join(base_dir, '*/')) if os.path.isdir(f)]
    
    # Create figures for plotting
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    
    # Plot voxel_numbers.csv
    for folder in experiment_folders:
        voxel_file_path = os.path.join(folder, 'voxel_numbers.csv')
        if os.path.exists(voxel_file_path):
            first_df = pd.read_csv(voxel_file_path)
            common_time = first_df['time_since_start']
            interpolated_values = read_and_interpolate_csv(voxel_file_path, common_time, 'time_since_start', 'num_of_voxels')
            folder_name = os.path.basename(os.path.normpath(folder))  # Get the lowest level of folder name
            plt.plot(common_time, interpolated_values, label=folder_name)
    
    # Add labels and legend for voxel_numbers.csv
    plt.xlabel('Time Since Start', fontsize=20)
    plt.ylabel('Number of Voxels', fontsize=20)
    plt.title('Number of Voxels Over Time', fontsize=20)
    plt.legend(fontsize=10)
    
    # Plot score
    plt.subplot(2, 1, 2)
    for folder in experiment_folders:
        voxel_file_path = os.path.join(folder, 'voxel_numbers.csv')
        semantic_file_path = os.path.join(folder, 'semantic_objects.csv')
        if os.path.exists(voxel_file_path) and os.path.exists(semantic_file_path):
            voxel_df = pd.read_csv(voxel_file_path)
            semantic_df = pd.read_csv(semantic_file_path)
            
            common_time = voxel_df['time_since_start']
            # common_path_length = semantic_df['path_length']
            voxel_numbers = read_and_interpolate_csv(voxel_file_path, common_time, 'time_since_start', 'num_of_voxels')
            view_angle_traversed = read_and_interpolate_csv(semantic_file_path, common_time, 'time_since_start', 'view_angle_traversed')
            
            score = 0.5 * (voxel_numbers / total_voxel) + 0.5 * (view_angle_traversed / total_view_angle)

            # Create a DataFrame with time_since_start, path_length, and score
            result_df = pd.DataFrame({
                'time_since_start': common_time,
                # 'path_length': common_path_length,
                'score': score
            })
            output_file_path = os.path.join(folder, 'processed_statistics.csv')
            result_df.to_csv(output_file_path, index=False)
            folder_name = os.path.basename(os.path.normpath(folder))  # Get the lowest level of folder name
            plt.plot(common_time, score, label=folder_name)
    
    # Add labels and legend for score
    plt.xlabel('Time Since Start', fontsize=20)
    plt.ylabel('Score', fontsize=20)
    plt.ylim(0, 1)
    plt.title('Score Over Time', fontsize=20)
    plt.legend(fontsize=10)
    
    # Show the plots
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()