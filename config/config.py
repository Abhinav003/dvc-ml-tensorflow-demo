
artifacts:
    ARTIFACTS_DIR: artifacts
    TRAINED_MODEL_DIR: model
    BASE_MODEL_DIR: base_model
    BASE_MODEL_NAME: VGG_base_model.h5
    UPDATED_BASE_MODEL_NAME: updated_VGG_base_model.h5
    CHECKPOINTS_DIR: checkpoints
    BASE_LOG_DIR: base_model_dir
    TENSORBOARD_ROOT_LOG_DIR: tensorboard_log_dir
    CALLBACKS_DIR: callbacks

source_download_paths:
    - ../DataSets/outside_data/dog
    - ../DataSets/outside_data/cat

local_data_dirs:
    - data/dog
    - data/cat
