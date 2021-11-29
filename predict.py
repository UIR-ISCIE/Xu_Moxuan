import os
import pickle
import tensorflow as tf
from utils import create_model, get_logger
from model import Model
from loader import input_from_line
from train import FLAGS, load_config
import pandas as pd

def main(_):
    config = load_config(FLAGS.config_file)
    logger = get_logger(FLAGS.log_file)
    # limit GPU memory
    tf_config = tf.ConfigProto()
    tf_config.gpu_options.allow_growth = False
    with open(FLAGS.map_file, "rb") as f:
        # tag_to_id, id_to_tag = pickle.load(f)
        char_to_id, id_to_char, tag_to_id, id_to_tag = pickle.load(f)
    with tf.Session(config=tf_config) as sess:
        model = create_model(sess, Model, FLAGS.ckpt_path, config, logger)
        # 该操作是：从终端手动输入数据进行预测
        while True:
            line = input("input sentence, please:")
            result = model.evaluate_line(sess, input_from_line(line, FLAGS.max_seq_len, tag_to_id), id_to_tag)
            print(result['entities'])

        # 下面的操作是：读取待训练的数据集，将一一对应的结果保存到文件中
        # with open('1.txt', 'r', encoding='utf-8') as f:
        #     lines = f.readlines()
        #
        # # f = open('2_1.txt','w',encoding='utf-8')
        # fp = open("1_1.csv", "w+", encoding='utf_8_sig')
        # #
        # for x in lines:
        #     result = model.evaluate_line(sess, input_from_line(x, FLAGS.max_seq_len, tag_to_id), id_to_tag)
        #     rs = result["string"], result["entities"]
        #     # print(type(rs)) #tuple元组类型
        #     re = str(rs[0]) + "\t" + str(rs[1])
        #     # print(rs)
        #     for i in re:
        #         fp.write(str(i))
        #     fp.write("\n")
        # fp.close()


if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    tf.app.run(main)
