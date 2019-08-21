
#include<atomic>
#include<array>

template<typename T, size_t size>
class LockFreeMultiQueue {
private:
    static constexpr size_t ringBufferSize = size  + 1;
    std::array<std::atomic<T>, ringBufferSize> ringBuffer;
    std::atomic<size_t> readPos = {0}, writePos = {0};

    static constexpr size_t getPositionAfter(size_t pos) noexcept {
        return ++pos == ringBufferSize? 0: pos;
    }
public:
    bool push (const T & newElement) {
        auto oldWritePos = writePos.load();
        auto newWritePos = getPositionAfter(oldWritePos);

        if (newWritePos == readPos.load()) {
            return false;
        }

        ringBuffer[oldWritePos].store(newElement);
        writePos.store(newWritePos);
        return true;
    }

    bool pop (T & resElement) {
        while (true) {
            auto oldWritePos = writePos.load();
            auto oldReadPos = readPos.load();
            if (oldWritePos == oldReadPos) {
                return false;
            }
            resElement = ringBuffer[oldReadPos].load();
            if (readPos.compare_exchange_strong(oldReadPos, getPositionAfter(oldReadPos))){
                return true;
            }
        }
    }

};