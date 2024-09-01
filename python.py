!pip install pytorch_lightning==1.8.6

!pip uninstall -y aitextgen
!pip install aitextgen==0.6.0

import os
os._exit(00)


# Install compatible versions of dependencies
!pip uninstall -y aitextgen
!pip install aitextgen==0.6.0
!pip install pytorch_lightning==1.8.6 transformers==4.42.4 torch==2.3.1

from aitextgen import aitextgen

# Initialize aitextgen with GPT-2 model
ai = aitextgen(tf_gpt2="124M", to_gpu=True)

# Train the model
ai.train("input.txt",
         line_by_line=True,
         from_cache=False,
         num_steps=2000,
         generate_every=100,
         save_every=500,
         save_gdrive=False,
         learning_rate=1e-3,
         fp16=False,
         batch_size=1, 
         )

# Generate text with the trained model
ai.generate(10, prompt="What a wonderful day")
