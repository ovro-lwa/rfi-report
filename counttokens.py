from llama.tokenizer import Tokenizer
import json

if __name__ == '__main__':
    with open("/home/pipeline/proj/lwa-shell/mnc_python/config/lwa_config_calim_interleave.yaml") as f:
        data = f.read()
    tk = Tokenizer('/opt/devel/yuping/llama/tokenizer.model')
    print(len(tk.encode(data, bos=False, eos=False)))
