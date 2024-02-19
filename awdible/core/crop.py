"""
Crop the audio
"""

# import ffmpeg

from awdible.logger import logger


class Crop:
    """Crop the audio if needed"""

    pass

    # @classmethod
    # def cut(
    #     self,
    #     fn: str,
    #     start: str,
    #     end: str,
    #     n_item: int | None,
    #     total_items: int | None,
    # ) -> str:
    #     """Crop the audio"""

    #     # pattern
    #     replacer = (
    #         fn.replace(".mp3", "_cut.mp3")
    #         if not (n_item or total_items)
    #         else fn.replace(".mp3", f"_cut_{n_item}_{total_items}.mp3")
    #     )

    #     # update out
    #     out = fn.replace(".mp3", replacer)

    #     # split
    #     ffmpeg.input(fn, ss=start, to=end).output(out).run()

    #     return out

    # @classmethod
    # def split(self, fn: str, n_splits=4) -> list[str]:
    #     """Crop the audio and return the list of the fn"""

    #     # len video
    #     len_seconds = self.video_duration(fn)

    #     # compute chunks
    #     chunks = self._build_chunks(len_seconds, n_splits)
    #     n_chunks = len(chunks)

    #     # perfom the cuts
    #     fn_list = []
    #     for i, (start, end) in enumerate(chunks):
    #         fn_chunk = Crop.cut(fn, start, end, i, n_chunks)
    #         fn_list.append(fn_chunk)

    #     return fn_list

    # @classmethod
    # def _build_chunks(self, len_seconds: int, n_splits: int) -> list[tuple]:
    #     """Build the chunks"""

    #     chunks = []

    #     # compute chunks
    #     for i in range(n_splits):
    #         start = i * len_seconds // n_splits
    #         end = (i + 1) * len_seconds // n_splits
    #         chunks.append((start, end))

    #     # -1 sec for each start except the first
    #     for i, (start, end) in enumerate(chunks):
    #         if not i:
    #             continue
    #         start -= 1
    #         chunks[i] = (start, end)

    #     # +1 sec for the last end
    #     chunks[-1] = (chunks[-1][0], chunks[-1][1] + 2)

    #     return chunks

    # @classmethod
    # def video_duration(self, fn):
    #     """Compute the video len"""

    #     len_seconds = ffmpeg.probe(fn)["format"]["duration"]
    #     len_seconds = int(float(len_seconds)) + 1

    #     return len_seconds
