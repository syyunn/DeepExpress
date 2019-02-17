def get_size_of_activation_pattern_fc(layer_width, layer_depth, input_dim):
    power = layer_depth * input_dim

    return layer_width ** power


if __name__ == "__main__":
    size_1 = get_size_of_activation_pattern_fc(4, 1, 2)

    for _layer_depth in range(3):
        print(get_size_of_activation_pattern_fc(4, _layer_depth, 2))
