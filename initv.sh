
valgrind \
  --leak-check=full \
  --show-leak-kinds=all \
  --track-origins=yes \
  --verbose \
  --log-file=reth_valgrind_output_init.txt \
  reth \
  init \
  --datadir=./execution-data \
  --chain=./el-cl-genesis-data/custom_config_data/genesis.json


