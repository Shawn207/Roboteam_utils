# Exploration_statistics
This is used for postprocessing and benchmarking exploration efficiency after running autonomous semantic exploration algorithm.
## Usage
Make sure running  ```map_explore_statistics``` node when running autonomous exploration algorithm. 
After running the algorithm, you should get 3 files:
- ```scores.csv```
- ```semantic_object.scv```
- ```voxel_numbers.csv```

Put them into folder structure like this:
```
Roboteam_utils
├──explore_statistics.py
├──data
│  ├──exp_1
│  │  ├──scores.csv
│  │  ├──semantic_object.csv
│  │  └──voxel_numbers.csv
│  ├──exp_2
│  │  ├──scores.csv
│  │  ├──semantic_object.csv
│  │  └──voxel_numbers.csv
|  ├──exp_3
|     ├──...
|     ├──...
|     └──...
└──...
```

where ```data``` can be any your custom folder containing all the experiments data, you can edit it in the ```explore_statistics.py``` file.

Then run the following command to get the statistics:
```
python3 explore_statistics.py
```

## Output
The output will be 2 plot, one is time vs score, the other is time vs voxel number. They are comparing among all experiments. Also, in each experiment folder, there will be a ```processd_statistics.csv``` file containing the time and final normalized score of each experiment.
