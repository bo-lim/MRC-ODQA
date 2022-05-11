from dataclasses import dataclass, field
from typing import Optional
from transformers import TrainingArguments, HfArgumentParser
import yaml

def return_arg():

    with open('./configs/training_args.yaml') as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)
    training_arguments, model_arguments, data_arguments, wandb_arguments = configs['TrainingArguments'], \
                                                          configs['ModelArguments'], \
                                                          configs['DataTrainingArguments'], \
                                                          configs['WandbArguments']

    model_args = ModelArguments(**model_arguments)
    data_args = DataTrainingArguments(**data_arguments)
    training_args = TrainingArguments(**training_arguments)
    wandb_args = WandbArguments(**wandb_arguments)

    return model_args, data_args, training_args, wandb_args

@dataclass
class ModelArguments:
    """
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune from.
    """

    model_name_or_path: str = field(
        default="klue/bert-base",
        metadata={
            "help": "Path to pretrained model or model identifier from huggingface.co/models"
        },
    )
    use_default: bool = field(
        default=True,
        metadata={
            "help": "Whether you use Default Model or change Classifier(False)"
        },
    )

    config_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "Pretrained config name or path if not the same as model_name"
        },
    )
    tokenizer_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "Pretrained tokenizer name or path if not the same as model_name"
        },
    )
    use_checkpoint: Optional[bool] = field(
        default=True,
        metadata={
            "help": "Use Checkpoint"
        },
    )

@dataclass
class WandbArguments:
    project: Optional[str] = field(
        default='mrc',
        metadata={"help": "Wandb Project Name"}
    )

    name: Optional[str] = field(
        default='No_Setting',
        metadata={"help": "Wandb Experiments Name"}
    )

    entity: Optional[str] = field(
        default='violetto',
        metadata={"help": "Wandb User Name"}
    )


@dataclass
class DataTrainingArguments:
    """
    Arguments pertaining to what data we are going to input our model for training and eval.
    """

    dataset_name: Optional[str] = field(
        default="../data/train_dataset",
        metadata={"help": "The name of the dataset to use."},
    )
    overwrite_cache: bool = field(
        default=False,
        metadata={"help": "Overwrite the cached training and evaluation sets"},
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None,
        metadata={"help": "The number of processes to use for the preprocessing."},
    )
    max_seq_length: int = field(
        default=384,
        metadata={
            "help": "The maximum total input sequence length after tokenization. Sequences longer "
            "than this will be truncated, sequences shorter will be padded."
        },
    )
    pad_to_max_length: bool = field(
        default=False,
        metadata={
            "help": "Whether to pad all samples to `max_seq_length`. "
            "If False, will pad the samples dynamically when batching to the maximum length in the batch (which can "
            "be faster on GPU but will be slower on TPU)."
        },
    )
    doc_stride: int = field(
        default=128,
        metadata={
            "help": "When splitting up a long document into chunks, how much stride to take between chunks."
        },
    )
    max_answer_length: int = field(
        default=30,
        metadata={
            "help": "The maximum length of an answer that can be generated. This is needed because the start "
            "and end predictions are not conditioned on one another."
        },
    )
    eval_retrieval: bool = field(
        default=True,
        metadata={"help": "Whether to run passage retrieval using sparse embedding."},
    )
    num_clusters: int = field(
        default=64, metadata={"help": "Define how many clusters to use for faiss."}
    )
    top_k_retrieval: int = field(
        default=10,
        metadata={
            "help": "Define how many top-k passages to retrieve based on similarity."
        },
    )
    use_faiss: bool = field(
        default=False, metadata={"help": "Whether to build with faiss"}
    )