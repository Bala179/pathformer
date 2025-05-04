if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi
seq_len=12
model_name=PathFormer

root_path_name=./dataset/retail
model_id_name=retail
data_name=custom

pred_len=10

data_path_name=cluster_1.csv
python -u run.py \
    --is_training 1 \
    --root_path $root_path_name \
    --data_path $data_path_name \
    --model_id $model_id_name_$data_path_name'_'$seq_len'_'$pred_len \
    --model $model_name \
    --data $data_name \
    --features MS \
    --freq d \
    --seq_len $seq_len \
    --pred_len $pred_len \
    --num_nodes 114 \
    --layer_nums 3 \
    --residual_connection 1\
    --k 2\
    --d_model 16 \
    --d_ff 128 \
    --patch_size_list 12 6 4 6 4 3 6 4 12 2 4 2 \
    --metric mape \
    --train_epochs 20 \
    --patience 10 \
    --lradj 'TST' \
    --pct_start 0.2 \
    --itr 1 \
    --batch_size 16 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'$data_path_name'_'$seq_len'_'$pred_len.log

data_path_name=cluster_5.csv
python -u run.py \
    --is_training 1 \
    --root_path $root_path_name \
    --data_path $data_path_name \
    --model_id $model_id_name_$data_path_name'_'$seq_len'_'$pred_len \
    --model $model_name \
    --data $data_name \
    --features MS \
    --freq d \
    --seq_len $seq_len \
    --pred_len $pred_len \
    --num_nodes 1959 \
    --layer_nums 3 \
    --residual_connection 1\
    --k 2\
    --d_model 16 \
    --d_ff 128 \
    --patch_size_list 12 6 4 6 4 3 6 4 12 2 4 2 \
    --metric mape \
    --train_epochs 20\
    --patience 10 \
    --lradj 'TST' \
    --pct_start 0.2 \
    --itr 1 \
    --batch_size 16 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'$data_path_name'_'$seq_len'_'$pred_len.log

data_path_name=cluster_7.csv
python -u run.py \
    --is_training 1 \
    --root_path $root_path_name \
    --data_path $data_path_name \
    --model_id $model_id_name_$data_path_name'_'$seq_len'_'$pred_len \
    --model $model_name \
    --data $data_name \
    --features MS \
    --freq d \
    --seq_len $seq_len \
    --pred_len $pred_len \
    --num_nodes 160 \
    --layer_nums 3 \
    --residual_connection 1\
    --k 2\
    --d_model 16 \
    --d_ff 128 \
    --patch_size_list 12 6 4 6 4 3 6 4 12 2 4 2 \
    --metric mape \
    --train_epochs 20\
    --patience 10 \
    --lradj 'TST' \
    --pct_start 0.2 \
    --itr 1 \
    --batch_size 16 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'$data_path_name'_'$seq_len'_'$pred_len.log