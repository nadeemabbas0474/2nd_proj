"""
Helper Script for Running Safe-HIL-RL on Google Colab
This script provides utility functions for managing the project on Colab
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


class ColabSetup:
    """Helper class for setting up Safe-HIL-RL on Google Colab"""
    
    def __init__(self, workspace="/content"):
        self.workspace = Path(workspace)
        self.hil_path = self.workspace / "Safe-Human-in-the-Loop-RL"
        self.smarts_path = self.workspace / "SMARTS"
        
    def mount_drive(self, drive_path="/content/drive"):
        """Mount Google Drive for persistent storage"""
        try:
            from google.colab import drive
            drive.mount(drive_path)
            print(f"✓ Google Drive mounted at {drive_path}")
            return True
        except Exception as e:
            print(f"⚠️ Failed to mount Google Drive: {e}")
            return False
    
    def setup_paths(self):
        """Add necessary paths to sys.path"""
        paths_to_add = [
            str(self.smarts_path),
            str(self.hil_path),
        ]
        
        for path in paths_to_add:
            if path not in sys.path and os.path.exists(path):
                sys.path.insert(0, path)
                print(f"✓ Added {path} to sys.path")
    
    def check_gpu(self):
        """Check GPU availability and CUDA setup"""
        try:
            import torch
            print(f"PyTorch version: {torch.__version__}")
            print(f"CUDA available: {torch.cuda.is_available()}")
            
            if torch.cuda.is_available():
                print(f"CUDA version: {torch.version.cuda}")
                print(f"GPU Device: {torch.cuda.get_device_name(0)}")
                print(f"Number of GPUs: {torch.cuda.device_count()}")
                return True
            else:
                print("⚠️ WARNING: GPU not available!")
                return False
        except ImportError:
            print("⚠️ PyTorch not installed")
            return False
    
    def save_checkpoint_to_drive(self, checkpoint_dir, drive_backup_dir):
        """Save checkpoints to Google Drive"""
        if not os.path.exists(checkpoint_dir):
            print(f"⚠️ Checkpoint directory not found: {checkpoint_dir}")
            return False
        
        try:
            os.makedirs(drive_backup_dir, exist_ok=True)
            shutil.copytree(checkpoint_dir, drive_backup_dir, dirs_exist_ok=True)
            print(f"✓ Checkpoints saved to {drive_backup_dir}")
            return True
        except Exception as e:
            print(f"⚠️ Failed to save checkpoints: {e}")
            return False
    
    def load_checkpoint_from_drive(self, drive_backup_dir, checkpoint_dir):
        """Load checkpoints from Google Drive"""
        if not os.path.exists(drive_backup_dir):
            print(f"⚠️ Backup directory not found: {drive_backup_dir}")
            return False
        
        try:
            os.makedirs(checkpoint_dir, exist_ok=True)
            shutil.copytree(drive_backup_dir, checkpoint_dir, dirs_exist_ok=True)
            print(f"✓ Checkpoints loaded from {drive_backup_dir}")
            return True
        except Exception as e:
            print(f"⚠️ Failed to load checkpoints: {e}")
            return False
    
    def update_config(self, config_path, updates):
        """Update config.yaml with new values"""
        try:
            import yaml
            
            if not os.path.exists(config_path):
                print(f"⚠️ Config file not found: {config_path}")
                return False
            
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            
            # Update config
            for key, value in updates.items():
                config[key] = value
                print(f"✓ Updated {key} = {value}")
            
            # Save updated config
            with open(config_path, 'w') as f:
                yaml.dump(config, f)
            
            print(f"✓ Config updated successfully")
            return True
            
        except Exception as e:
            print(f"⚠️ Failed to update config: {e}")
            return False
    
    def create_backup(self, source_dirs, backup_name="backup.zip"):
        """Create a zip backup of specified directories"""
        try:
            import zipfile
            
            with zipfile.ZipFile(backup_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for source_dir in source_dirs:
                    if os.path.exists(source_dir):
                        for root, dirs, files in os.walk(source_dir):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, os.path.dirname(source_dir))
                                zipf.write(file_path, arcname)
                        print(f"✓ Added {source_dir} to backup")
                    else:
                        print(f"⚠️ Directory not found: {source_dir}")
            
            print(f"✓ Backup created: {backup_name}")
            return True
            
        except Exception as e:
            print(f"⚠️ Failed to create backup: {e}")
            return False
    
    def monitor_training(self, log_file):
        """Monitor training progress from log file"""
        if not os.path.exists(log_file):
            print(f"⚠️ Log file not found: {log_file}")
            return
        
        try:
            with open(log_file, 'r') as f:
                lines = f.readlines()
                # Print last 20 lines
                print("Last 20 lines of training log:")
                print("=" * 80)
                for line in lines[-20:]:
                    print(line.strip())
                print("=" * 80)
        except Exception as e:
            print(f"⚠️ Failed to read log file: {e}")


def quick_setup():
    """Quick setup function for Colab"""
    print("=" * 80)
    print("Safe Human-in-the-Loop RL - Colab Quick Setup")
    print("=" * 80)
    
    setup = ColabSetup()
    
    # Check GPU
    print("\n1. Checking GPU...")
    setup.check_gpu()
    
    # Setup paths
    print("\n2. Setting up Python paths...")
    setup.setup_paths()
    
    # Mount Drive
    print("\n3. Mounting Google Drive...")
    setup.mount_drive()
    
    print("\n✓ Quick setup complete!")
    print("=" * 80)
    
    return setup


def save_progress(setup, drive_dir="/content/drive/MyDrive/SafeHIL_Results"):
    """Save all progress to Google Drive"""
    print("Saving progress to Google Drive...")
    
    dirs_to_save = [
        "logs",
        "models", 
        "checkpoints",
        "results",
        "outputs"
    ]
    
    os.makedirs(drive_dir, exist_ok=True)
    
    for dir_name in dirs_to_save:
        if os.path.exists(dir_name):
            target = os.path.join(drive_dir, dir_name)
            try:
                shutil.copytree(dir_name, target, dirs_exist_ok=True)
                print(f"✓ Saved {dir_name}/ to Drive")
            except Exception as e:
                print(f"⚠️ Failed to save {dir_name}: {e}")
    
    print(f"\n✓ Progress saved to {drive_dir}")


def load_progress(setup, drive_dir="/content/drive/MyDrive/SafeHIL_Results"):
    """Load progress from Google Drive"""
    print("Loading progress from Google Drive...")
    
    if not os.path.exists(drive_dir):
        print(f"⚠️ No saved progress found at {drive_dir}")
        return
    
    dirs_to_load = [
        "logs",
        "models",
        "checkpoints", 
        "results",
        "outputs"
    ]
    
    for dir_name in dirs_to_load:
        source = os.path.join(drive_dir, dir_name)
        if os.path.exists(source):
            try:
                shutil.copytree(source, dir_name, dirs_exist_ok=True)
                print(f"✓ Loaded {dir_name}/ from Drive")
            except Exception as e:
                print(f"⚠️ Failed to load {dir_name}: {e}")
    
    print("\n✓ Progress loaded from Drive")


# Example usage
if __name__ == "__main__":
    # Quick setup
    setup = quick_setup()
    
    # Example: Update config for training
    # setup.update_config("config.yaml", {"mode": "training", "epochs": 100})
    
    # Example: Save progress
    # save_progress(setup)
    
    # Example: Load progress
    # load_progress(setup)
