# Safe Human-in-the-Loop RL - Google Colab Setup Guide

This guide will help you run the Safe Human-in-the-Loop RL project on Google Colab after your remote GPU connection broke.

## 📋 Prerequisites

- Google account (for Google Colab)
- Google Drive (recommended for saving progress)
- Basic understanding of Jupyter notebooks

## 🚀 Quick Start

### Option 1: Use the Jupyter Notebook (Recommended)

1. **Upload the notebook to Google Colab:**
   - Download `Safe_HIL_RL_Colab_Setup.ipynb` from this repository
   - Go to [Google Colab](https://colab.research.google.com/)
   - Click `File` → `Upload notebook`
   - Upload the `Safe_HIL_RL_Colab_Setup.ipynb` file

2. **Enable GPU:**
   - Click `Runtime` → `Change runtime type`
   - Select `GPU` (T4, V100, or A100 if available)
   - Click `Save`

3. **Run the notebook:**
   - Execute cells sequentially from top to bottom
   - Each cell has explanations and will guide you through the setup

### Option 2: Manual Setup

If you prefer manual setup, follow these steps:

## 📝 Step-by-Step Manual Setup

### Step 1: Create a New Colab Notebook

1. Go to [Google Colab](https://colab.research.google.com/)
2. Create a new notebook
3. Enable GPU: `Runtime` → `Change runtime type` → `GPU`

### Step 2: Check GPU Availability

```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")
!nvidia-smi
```

### Step 3: Install System Dependencies

```bash
%%bash
apt-get update -qq
apt-get install -y -qq \
    libspatialindex-dev \
    xorg libx11-dev libglu1-mesa-dev libgl1-mesa-dev \
    libxrandr-dev libxxf86vm-dev libxcursor-dev \
    libxi-dev libxinerama-dev libxrender-dev \
    mesa-utils xvfb ffmpeg
```

### Step 4: Clone the Repository

```python
import os

WORKSPACE = "/content"
os.chdir(WORKSPACE)

# Clone Safe-HIL-RL
!git clone https://github.com/OscarHuangWind/Safe-Human-in-the-Loop-RL.git
os.chdir("Safe-Human-in-the-Loop-RL")
print(f"Current directory: {os.getcwd()}")
```

### Step 5: Install PyTorch with CUDA

```python
# Install PyTorch with CUDA support
!pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Verify
import torch
print(f"PyTorch {torch.__version__} installed")
print(f"CUDA available: {torch.cuda.is_available()}")
```

### Step 6: Install Python Dependencies

```python
# Install common RL dependencies
!pip install -q numpy pandas matplotlib seaborn gym gymnasium pyyaml tensorboard
!pip install -q opencv-python pillow scipy scikit-learn
```

### Step 7: Clone and Install SMARTS

```python
os.chdir(WORKSPACE)

# Clone SMARTS
!git clone https://github.com/huawei-noah/SMARTS.git
os.chdir("SMARTS")

# Checkout comp-1 branch
!git checkout comp-1

# Install SMARTS
!pip install -q -e '.[camera_obs,test,train]'
!pip install -q -e '.[extras]'

# Verify installation
import smarts
print(f"SMARTS version: {smarts.__version__}")
```

### Step 8: Build the Scenario

```python
os.chdir(f"{WORKSPACE}/Safe-Human-in-the-Loop-RL")

# Build scenario
!scl scenario build --clean scenario/straight/
```

### Step 9: Setup Virtual Display

```python
!pip install -q pyvirtualdisplay

from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()
print("Virtual display started!")
```

### Step 10: Fix Python Paths

```python
import sys

# Add paths
smarts_path = f"{WORKSPACE}/SMARTS"
hil_path = f"{WORKSPACE}/Safe-Human-in-the-Loop-RL"

sys.path.insert(0, smarts_path)
sys.path.insert(0, hil_path)

print("Paths configured!")
```

### Step 11: Mount Google Drive (Optional but Recommended)

```python
from google.colab import drive
drive.mount('/content/drive')

# Create backup directory
!mkdir -p /content/drive/MyDrive/SafeHIL_Results
```

### Step 12: Run Training

```python
os.chdir(f"{WORKSPACE}/Safe-Human-in-the-Loop-RL")

# Run training
!python main.py
```

### Step 13: Save Results to Google Drive

```python
# Save results to Drive
!cp -r logs/ /content/drive/MyDrive/SafeHIL_Results/ 2>/dev/null || true
!cp -r models/ /content/drive/MyDrive/SafeHIL_Results/ 2>/dev/null || true
!cp -r checkpoints/ /content/drive/MyDrive/SafeHIL_Results/ 2>/dev/null || true

print("Results saved to Google Drive!")
```

## 🔧 Configuration

### Training Mode

The default mode is training. To modify training parameters, edit `config.yaml`:

```python
import yaml

with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

# Modify parameters
config['mode'] = 'training'
config['epochs'] = 100  # Example
config['batch_size'] = 32  # Example

with open("config.yaml", 'w') as f:
    yaml.dump(config, f)
```

### Evaluation Mode

To switch to evaluation mode:

```python
import yaml

with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

config['mode'] = 'evaluation'

with open("config.yaml", 'w') as f:
    yaml.dump(config, f)

# Run evaluation
!python main.py
```

## 📊 Monitoring Training

### Using TensorBoard

```python
%load_ext tensorboard
%tensorboard --logdir logs/
```

### View Training Logs

```python
# View last 50 lines of log
!tail -50 logs/training.log
```

## 💾 Saving and Loading Progress

### Save Progress

```python
# Use the helper script
from colab_helper_script import save_progress, ColabSetup

setup = ColabSetup()
save_progress(setup, "/content/drive/MyDrive/SafeHIL_Results")
```

### Load Progress

```python
from colab_helper_script import load_progress, ColabSetup

setup = ColabSetup()
load_progress(setup, "/content/drive/MyDrive/SafeHIL_Results")
```

### Download Results Locally

```python
from google.colab import files

# Create zip archive
!zip -r results.zip logs/ models/ checkpoints/ results/

# Download
files.download('results.zip')
```

## ⚠️ Important Limitations on Colab

### What Works:
✅ Training base models (without human guidance)  
✅ Evaluation of trained models  
✅ TensorBoard visualization  
✅ Saving/loading checkpoints  
✅ GPU acceleration  

### What Doesn't Work:
❌ **Human Guidance Features**: Keyboard control and G29 steering wheel (no interactive input in Colab)  
❌ **Envision Visualization**: The web-based visualization at localhost:8081 is not accessible  
❌ **Real-time Interaction**: Cannot provide human demonstrations during training  

### Workarounds:
1. **Train base models** on Colab without human guidance
2. **Download trained models** to your local machine
3. **Continue with human guidance** on your local machine with GPU
4. **Use Colab** for hyperparameter tuning and experiments

## 🔄 Handling Disconnections

Colab sessions can disconnect due to:
- Inactivity timeout (90 minutes for free tier)
- Maximum session length (12 hours for free tier)
- Network issues

### To Resume After Disconnect:

1. **If you saved to Google Drive:**
   ```python
   # Mount Drive
   from google.colab import drive
   drive.mount('/content/drive')
   
   # Load progress
   from colab_helper_script import load_progress, ColabSetup
   setup = ColabSetup()
   load_progress(setup, "/content/drive/MyDrive/SafeHIL_Results")
   
   # Continue training
   !python main.py
   ```

2. **If you didn't save:**
   - Unfortunately, you'll need to restart from Step 1
   - **Always save to Google Drive periodically!**

### Auto-Save Strategy:

Add this to your training script to auto-save every N epochs:

```python
# Add to your training loop
if epoch % 10 == 0:  # Save every 10 epochs
    from colab_helper_script import save_progress, ColabSetup
    setup = ColabSetup()
    save_progress(setup, "/content/drive/MyDrive/SafeHIL_Results")
```

## 🐛 Troubleshooting

### Issue: CUDA Out of Memory

**Solution:**
```python
# Reduce batch size in config.yaml
import yaml
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)
config['batch_size'] = 16  # Reduce from 32
with open("config.yaml", 'w') as f:
    yaml.dump(config, f)
```

### Issue: SMARTS Installation Fails

**Solution:**
```bash
# Reinstall system dependencies
!apt-get update
!apt-get install -y libspatialindex-dev
!pip install --upgrade pip setuptools wheel
!pip install -e '.[camera_obs,test,train]'
```

### Issue: Module Not Found

**Solution:**
```python
import sys
sys.path.insert(0, "/content/SMARTS")
sys.path.insert(0, "/content/Safe-Human-in-the-Loop-RL")
```

### Issue: Scenario Build Fails

**Solution:**
```bash
# Check if scenario directory exists
!ls -la scenario/

# Rebuild scenario
!scl scenario build --clean scenario/straight/
```

### Issue: Display/Rendering Errors

**Solution:**
```python
# Restart virtual display
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()
```

## 📈 Performance Tips

1. **Use GPU Runtime**: Always enable GPU for faster training
2. **Batch Size**: Adjust based on GPU memory (16-32 for T4, 32-64 for V100)
3. **Save Frequently**: Save to Google Drive every 10-20 epochs
4. **Monitor Memory**: Use `!nvidia-smi` to check GPU memory usage
5. **Close Unused Notebooks**: Only keep one Colab notebook running at a time

## 🎯 Recommended Workflow

1. **Initial Setup** (15-20 minutes):
   - Run the Jupyter notebook cells 1-11
   - Mount Google Drive
   - Verify GPU is working

2. **Training** (varies):
   - Start training with base model
   - Monitor with TensorBoard
   - Save checkpoints every 10 epochs

3. **Evaluation**:
   - Switch to evaluation mode
   - Test trained models
   - Download results

4. **Local Continuation**:
   - Download trained models
   - Continue with human guidance on local machine

## 📚 Additional Resources

- [SMARTS Documentation](https://github.com/huawei-noah/SMARTS)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Original Repository](https://github.com/OscarHuangWind/Safe-Human-in-the-Loop-RL)

## 💡 Tips for Success

1. **Start Small**: Test with fewer epochs first to ensure everything works
2. **Monitor Actively**: Check training progress regularly
3. **Save Often**: Don't lose hours of training due to disconnection
4. **Use Colab Pro**: Consider upgrading for longer sessions and better GPUs
5. **Backup Everything**: Keep copies of trained models in multiple locations

## 🆘 Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Review error messages carefully
3. Check SMARTS GitHub issues
4. Verify all dependencies are installed correctly

## 📝 Notes

- Free Colab has usage limits; consider Colab Pro for intensive training
- GPU availability is not guaranteed on free tier
- Sessions are stateless; always save your work
- Human guidance features require local setup with input devices

---

**Good luck with your training! 🚀**
