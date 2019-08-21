
template<typename T, size_t size>
class LockFreeMultiQueue {
    // 单个消费者的实现
    private:
        static constexpr size_t ringBufferSize = size  + 1;
        std::array<std::atomic<T>, ringBufferSize> ringBuffer;
        std::atomic<size_t> readPos = {0}, wirtePos = {0};

        static constexpr size_t getPosiitionAfter(size_t pos) noexcept {
            return ++pos == ringBufferSize? 0: pos;
        }
        public:
        bool push (const T & newElement) {
            auto oldWritePos = wirtePos.load();
            auto newWritePos = getPosiitionAfter(oldWritePos);

            if (newWritePos == readPos.load()) {
                return false;
            }

            ringBuffer[oldWritePos].store(newElement);
        }

        bool pop (T & resElement) {
                while (true) {
                auto oldWritePos = wirtePos.load();
                auto oldReadPos = readPos.load();
                if (oldWritePos == oldReadPost) {
                    return false;
                }
                resElement = ringBuffer[oldReadPos].load();
                if (readPos.compare_exchange_strong(oldReadPos, getPosiitionAfter(oldReadPos))){
                    return true;
                }
            }

            return true;
        }
    
};