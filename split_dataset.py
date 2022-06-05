import splitfolders

source_folder = 'TomatoDataset'
target_folder = 'TomatoDatasetSplitted'

train_ratio = .8
val_ratio = .1
test_ratio = .1

seed = 1337
group_prefix = None
move = False

splitfolders.ratio(source_folder, output=target_folder, seed=seed, ratio=(train_ratio, val_ratio, test_ratio), group_prefix=group_prefix, move=move)