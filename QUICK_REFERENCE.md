# Safe-HIL-RL Colab - Quick Reference Card

## 🚀 Quick Start (Copy-Paste Ready)

### 1. Enable GPU
```
Runtime → Change runtime type → GPU → Save
```

### 2. One-Command Setup
```python
# Run this first!
!apt-get update -qq && apt-get install -y -qq libspatialindex-dev xorg libx11-dev libglu1-mesa-dev libgl1-mesa-dev xvfb ffmpeg
!pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install -q numpy pandas matplotlib seaborn gym gymnasium pyyaml tensorboard opencv-python pillow scipy scikit-learn pyvirtualdisplay

import os
os.chdir("/content")
!git clone https://github.com/OscarHuangWind/Safe-Human-in-the-Loop-RL.git
!git clone https://github.com/huawei-noah/SMARTS.git

os.chdir("/content/SMARTS")
!git checkout comp-1
!pip install -q -e '.[camera_obs,test,train]' && pip install -q -e '.[extras]'

os.chdir("/content/Safe-Human-in-the-Loop-RL")
!scl scenario build --clean scenario/straight/

from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()

import sys
sys.path.insert(0, "/content/SMARTS")
sys.path.insert(0, "/content/Safe-Human-in-the-Loop-RL")

print("✓ Setup complete! Ready to train.")
```

### 3. Mount Google Drive (Recommended)
```python
from google.colab import drive
drive.mount('/content/drive')
!mkdir -p /content/drive/MyDrive/SafeHIL_Results
```

### 4. Start Training
```python
os.chdir("/content/Safe-Human-in-the-Loop-RL")
!python main.py
```

## 💾 Save/Load Commands

### Save Progress
```python
!cp -r logs/ /content/drive/MyDrive/SafeHIL_Results/
!cp -r models/ /content/drive/MyDrive/SafeHIL_Results/
!cp -r checkpoints/ /content/drive/MyDrive/SafeHIL_Results/
print("✓ Saved to Drive")
```

### Load Progress
```python
!cp -r /content/drive/MyDrive/SafeHIL_Results/logs/ ./
!cp -r /content/drive/MyDrive/SafeHIL_Results/models/ ./
!cp -r /content/drive/MyDrive/SafeHIL_Results/checkpoints/ ./
print("✓ Loaded from Drive")
```

### Download Locally
```python
from google.colab import files
!zip -r results.zip logs/ models/ checkpoints/
files.download('results.zip')
```

## 🔧 Configuration Commands

### Switch to Evaluation Mode
```python
import yaml
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)
config['mode'] = 'evaluation'
with open("config.yaml", 'w') as f:
    yaml.dump(config, f)
!python main.py
```

### Reduce Batch Size (if OOM)
```python
import yaml
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)
config['batch_size'] = 16
with open("config.yaml", 'w') as f:
    yaml.dump(config, f)
```

## 📊 Monitoring Commands

### Check GPU
```python
!nvidia-smi
```

### View Logs
```python
!tail -50 logs/training.log
```

### TensorBoard
```python
%load_ext tensorboard
%tensorboard --logdir logs/
```

### Check Training Progress
```python
!ls -lh models/
!ls -lh checkpoints/
```

## 🔄 Recovery After Disconnect

```python
# 1. Mount Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Navigate to project
import os
os.chdir("/content/Safe-Human-in-the-Loop-RL")

# 3. Load saved progress
!cp -r /content/drive/MyDrive/SafeHIL_Results/* ./

# 4. Fix paths
import sys
sys.path.insert(0, "/content/SMARTS")
sys.path.insert(0, "/content/Safe-Human-in-the-Loop-RL")

# 5. Restart virtual display
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()

# 6. Continue training
!python main.py
```

## 🐛 Quick Fixes

### Fix: Module Not Found
```python
import sys
sys.path.insert(0, "/content/SMARTS")
sys.path.insert(0, "/content/Safe-Human-in-the-Loop-RL")
```

### Fix: CUDA OOM
```python
import yaml
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)
config['batch_size'] = 16
with open("config.yaml", 'w') as f:
    yaml.dump(config, f)
```

### Fix: Display Error
```python
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()
```

### Fix: SMARTS Not Found
```python
os.chdir("/content/SMARTS")
!pip install -e '.[camera_obs,test,train]'
```

## 📋 Useful Checks

### Verify Installation
```python
import torch
import smarts
print(f"PyTorch: {torch.__version__}")
print(f"CUDA: {torch.cuda.is_available()}")
print(f"SMARTS: {smarts.__version__}")
print(f"GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")
```

### Check Files
```python
!ls -la
!ls -la scenario/
!ls -la logs/
!ls -la models/
```

### Check Disk Space
```python
!df -h
```

### Check Memory
```python
!free -h
!nvidia-smi
```

## ⏱️ Time Estimates

- Initial Setup: 15-20 minutes
- Scenario Build: 2-5 minutes
- Training (depends on config): 1-8 hours
- Evaluation: 10-30 minutes

## 🎯 Best Practices

1. **Save every 10 epochs**: Add auto-save to training loop
2. **Monitor GPU memory**: Run `!nvidia-smi` periodically
3. **Use smaller batches**: Start with batch_size=16
4. **Test first**: Run 1-2 epochs to verify setup
5. **Keep Drive mounted**: Don't unmount during training

## 📞 Emergency Commands

### Kill Training
```python
# Press the Stop button in Colab, or:
import os
import signal
os.kill(os.getpid(), signal.SIGTERM)
```

### Clear Memory
```python
import gc
import torch
gc.collect()
torch.cuda.empty_cache()
```

### Restart Runtime
```
Runtime → Restart runtime
```

## 🔗 Important Paths

- Project: `/content/Safe-Human-in-the-Loop-RL`
- SMARTS: `/content/SMARTS`
- Drive: `/content/drive/MyDrive/SafeHIL_Results`
- Logs: `./logs/`
- Models: `./models/`
- Checkpoints: `./checkpoints/`

## 📝 Notes

- Free Colab: 12-hour max session, 90-min idle timeout
- GPU not guaranteed on free tier
- Save to Drive every 30 minutes
- Download important results immediately

---

**Keep this reference handy while working in Colab! 📌**
