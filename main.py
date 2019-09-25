model.compile(optimizer=Adam(lr=1e-4), loss='binary_crossentropy', metrics=['accuracy'])

# model.summary()

if (pretrained_weights):
    model.load_weights(pretrained_weights)