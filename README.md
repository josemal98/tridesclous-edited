# Tridesclous-edited: Modified Version for Real-Time Neural Analysis Interface

🔬 **Modified version of tridesclous for Real-Time Neural Analysis Interface**

[![Version](https://img.shields.io/badge/version-1.6.8--neural--interface-blue.svg)](https://github.com/josemal98/tridesclous-edited)
[![Original](https://img.shields.io/badge/based%20on-tridesclous%201.6.8-green.svg)](https://github.com/tridesclous/tridesclous)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🎯 Overview

This is a **modified version** of [tridesclous](https://github.com/tridesclous/tridesclous) specifically enhanced for the **Real-Time Neural Analysis Interface** project. The modifications focus on improving real-time spike detection capabilities, PyACQ stream integration, and debugging features.

## 🚀 Key Modifications

### **Enhanced OnlinePeeler (`online/onlinepeeler.py`)**
- ✅ **Robust PyACQ Stream Parameter Handling**: Added timeout-based waiting for stream parameters
- ✅ **Callback System**: Enhanced callback mechanism for real-time data processing
- ✅ **Detailed Logging**: Comprehensive debug logging for spike detection monitoring
- ✅ **Stream Synchronization**: Improved synchronization between PyACQ streams and tridesclous processing

### **Main Changes vs Original v1.6.8**
```python
# Enhanced parameter waiting with timeout
for _ in range(50):  # Wait up to 5 seconds
    if hasattr(self.input, 'params') and 'sample_rate' in self.input.params:
        break
    time.sleep(0.1)

# Enhanced callback system
if hasattr(self, '_signal_callback') and callable(self._signal_callback):
    self._signal_callback(preprocessed_chunk, sig_index)
    
if hasattr(self, '_spike_callback') and callable(self._spike_callback):
    self._spike_callback(spikes, total_spike)
```

## 📋 Installation

### **For Real-Time Neural Analysis Interface Project**
This version is automatically installed when setting up the neural analysis environment:

```bash
# Clone the main project
git clone https://github.com/josemal98/Real-Time_Neural_Analysis_Interface.git

# Create environment with modified dependencies
conda env create -f trides_env.yml
```

### **Standalone Installation**
```bash
pip install git+https://github.com/josemal98/tridesclous-edited.git
```

## 🔧 Usage

This modified version maintains full compatibility with original tridesclous usage while providing enhanced real-time capabilities:

```python
from tridesclous import OnlinePeeler
# Enhanced version with improved PyACQ integration
# and real-time spike detection capabilities
```

## 📊 Compatibility

- **Base Version**: tridesclous 1.6.8
- **Python**: 3.7+
- **PyACQ**: Compatible with custom PyACQ fork
- **Real-Time Processing**: ✅ Enhanced
- **Original API**: ✅ Fully compatible

## 🔍 Detailed Modifications

### **1. PeelerThread Enhancements**
- Added comprehensive logging system for debugging
- Enhanced spike detection monitoring
- Improved callback mechanism for wrapper nodes

### **2. Stream Parameter Management**
- Robust handling of PyACQ stream parameters
- Timeout-based parameter waiting
- Better error handling and diagnostics

### **3. Real-Time Processing**
- Optimized for real-time neural signal processing
- Enhanced synchronization with external data sources
- Improved performance monitoring

## 🚦 Status

- ✅ **Functional**: All original tridesclous features work
- ✅ **Enhanced**: Real-time processing capabilities improved  
- ✅ **Tested**: Validated with Real-Time Neural Analysis Interface
- ✅ **Maintained**: Updated for project-specific requirements

## 📚 Related Projects

- **Main Project**: [Real-Time Neural Analysis Interface](https://github.com/josemal98/Real-Time_Neural_Analysis_Interface)
- **Original Library**: [tridesclous](https://github.com/tridesclous/tridesclous)
- **PyACQ Fork**: [pyacq-neural-analysis](https://github.com/josemal98/pyacq)

## 📄 License

This project maintains the same MIT license as the original tridesclous library.

## 🙏 Acknowledgments

- Original **tridesclous** team for the excellent spike sorting library
- Modifications made specifically for **Real-Time Neural Analysis Interface** project requirements

---

**⚠️ Note**: This is a specialized version. For general tridesclous usage, please use the [original repository](https://github.com/tridesclous/tridesclous).